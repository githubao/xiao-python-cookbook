#!/usr/bin/env python
# encoding: utf-8

"""
@description: 导入远程模块

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec11_url_import.py
@time: 2017/3/20 10:04
"""

import requests
import sys
import importlib
import types
import importlib.abc

from urllib.error import HTTPError, URLError
from html.parser import HTMLParser
import logging

log = logging.getLogger(__name__)


def load_module(url):
    response = requests.get(url)
    src = response.content.decode()
    mod = sys.modules.setdefault(url, types.ModuleType(url))
    code = compile(src, url, 'exec')
    mod.__file__ = url
    mod.__package__ = ''
    exec(code, mod.__dict__)
    return mod


def _get_links(url):
    class LinkParser(HTMLParser):
        def handle_starttag(self, tag, attrs):
            if tag == 'a':
                attrs = dict(attrs)
                links.add(attrs.get('href').rstrip('/'))

    links = set()

    try:
        log.debug('Getting links from {}'.format(url))
        response = requests.get(url)
        parser = LinkParser()
        parser.feed(response.content.decode())
    except Exception as e:
        log.debug('Could not get links. {}'.format(e))
    log.debug('links: ', links)
    return links


class UrlMetaFinder(importlib.abc.MetaPathFinder):
    def __init__(self, baseurl):
        self._baseurl = baseurl
        self._links = {}
        self._loaders = {baseurl: UrlModuleLoader(baseurl)}

    def find_module(self, fullname, path=None):
        log.debug('find_module: fullname={}, path={}'.format(fullname, path))
        if path == None:
            baseurl = self._baseurl
        else:
            if not path[0].startswith(self._baseurl):
                return None
            baseurl = path[0]

        parts = fullname.split('.')
        basename = parts[-1]
        log.debug('find_module: baseurl={}, basename={}'.format(baseurl, basename))

        if basename not in self._links:
            self._links[baseurl] = _get_links(baseurl)

        if basename in self._links[baseurl]:
            log.debug('find_module: trying package {}'.format(fullname))
            fullurl = self._baseurl + '/' + basename
            loader = UrlPackageLoader(fullurl)

            try:
                loader.load_module(fullname)
                self._links[fullurl] = _get_links(fullurl)
                self._loaders[fullurl] = UrlModuleLoader(fullurl)
                log.debug('find_module: package {} loaded'.format(fullname))
            except ImportError as e:
                log.debug('find_module: module {} found'.format(fullname))
                loader = None
            return loader

        filename = basename + '.py'
        if filename in self._links[baseurl]:
            log.debug('find_module: module {} found'.format(fullname))
            return self._loaders[baseurl]
        else:
            log.debug('find_module: module {} not found'.format(fullname))
            return None

    def invalidate_caches(self):
        log.debug('invalidating link cache')
        self._links.clear()


class UrlModuleLoader(importlib.abc.SourceLoader):
    def __init__(self, baseurl):
        self._baseurl = baseurl
        self._source_cache = {}

    def module_repr(self, module):
        return '<urlmodule {} from {}>'.format(module.__name__, module.__file__)

    def load_module(self, fullname):
        code = self.get_code(fullname)
        mod = sys.modules.setdefault(fullname, types.ModuleType(fullname))
        mod.__file__ = self.get_filename(fullname)
        mod.__loader__ = self
        mod.__package__ = fullname.rpartition('.')[0]
        exec(code, mod.__dict__)

        return mod

    def get_code(self, fullname):
        src = self.get_source(fullname)
        return compile(src, self.get_filename(fullname), 'exec')

    def get_data(self, path):
        pass

    def get_filename(self, fullname):
        return self._baseurl + '/' + fullname.split('.')[-1] + ".py"

    def get_source(self, fullname):
        filename = self.get_filename(fullname)
        log.debug('loader: reading {}'.format(filename))
        if filename in self._source_cache:
            log.debug('loader: cached {}'.format(filename))
            return self._source_cache[filename]
        try:
            response = requests.get(filename)
            source = response.content.decode()
            log.debug('loader: {} loaded'.format(filename))
            self._source_cache[filename] = source
            return source
        except (HTTPError, URLError) as e:
            log.debug('loader: {} failed. {}'.format(filename, e))
            raise ImportError('can not load {}'.format(filename))

    def is_package(self, fullname):
        return False


class UrlPackageLoader(UrlModuleLoader):
    def load_module(self, fullname):
        mod = super().load_module(fullname)
        mod.__path__ = [self._baseurl]
        mod.__package__ = fullname

    def get_filename(self, fullname):
        return self._baseurl + '/' + '__init__.py'

    def is_package(self, fullname):
        return True


_installed_meta_cache = {}


def install_meta(address):
    if address not in _installed_meta_cache:
        finder = UrlMetaFinder(address)
        _installed_meta_cache[address] = finder
        sys.meta_path.append(finder)
        log.debug('{} installed on sys.meta_path'.format(finder))


def remove_meta(address):
    if address in _installed_meta_cache:
        finder = _installed_meta_cache.pop(address)
        sys.meta_path.remove(finder)
        log.debug('{} removed from sys.meta_path', finder)


class UrlPathFinder(importlib.abc.PathEntryFinder):
    def __init__(self, baseurl):
        self._links = None
        self._loader = UrlModuleLoader(baseurl)
        self._baseurl = baseurl

    def find_loader(self, fullname):
        log.debug('find_loader: {}'.format(fullname))
        parts = fullname.split('.')
        basename = parts[-1]
        if self._links is None:
            self._links = []
            self._links = _get_links(self._baseurl)

        if basename in self._links:
            log.debug('find_loader: trying package {}'.format(fullname))
            fullurl = self._baseurl + '/' + basename
            loader = UrlPackageLoader(fullurl)

            try:
                loader.load_module(fullname)
                log.debug('find_loader: package {} loaded'.format(fullname))
            except ImportError as e:
                log.debug('find_loader: {} is a namespace package'.format(fullname))
                loader = None
            return (loader, [fullurl])

        filename = basename + '.py'
        if filename in self._links:
            log.debug('find_loader: module {} found', fullname)
            return (self._loader, [])
        else:
            log.debug('find_loader: module {} not found'.format(fullname))
            return (None, [])

    def invalidate_caches(self):
        log.debug('invalidating link cacke')
        self._links = None


_url_path_cache = {}


def handle_url(path):
    if path.startswith(('http://', 'https://')):
        log.debug('Handle path? {}. [Yes]'.format(path))
        if path in _url_path_cache:
            finder = _url_path_cache[path]
        else:
            finder = UrlPathFinder(path)
            _url_path_cache[path] = finder
        return finder
    else:
        log.debug('Handle path? {}. [No]'.format(path))


def install_path_hook():
    sys.path_hooks.append(handle_url)
    sys.path_importer_cache.clear()
    log.debug('Installing handle_url')


def remove_path_hook():
    sys.path_hooks.remove(handle_url)
    sys.path_importer_cache.clear()
    log.debug('Removing handle_url')


def run():
    spam = load_module('http://localhost:15000/spam.py')
    spam.hello('xiao')


def run2():
    install_meta('http://localhost:15000')
    import spam


def run3():
    install_path_hook()
    sys.path.append('http://localhost:15000')
    import spam


class Finder:
    def find_module(self, fullname, path):
        print('Looking for ', fullname, path)
        return None

sys.meta_path.insert(0, Finder())
def finder():
    import math
    import threading


def demo():
    from pprint import pprint
    pprint(sys.meta_path)


def get():
    response = requests.get('http://localhost:15000/fib.py')
    print(response.content.decode())


def main():
    # get()
    # run()
    # run2()
    # run3()
    # demo()
    finder()


if __name__ == '__main__':
    main()
