#!/usr/bin/env python
# encoding: utf-8

"""
@description: 缓存实例的处理

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec25_cached_instance.py
@time: 2017/3/2 18:39
"""

import weakref


class Spam:
    def __init__(self, name):
        self.name = name


_spam_cache = weakref.WeakValueDictionary()


def get_spam(name):
    if name not in _spam_cache:
        s = Spam(name)
        _spam_cache[name] = s
    else:
        s = _spam_cache[name]
    return s


class Spam2:
    _spam_cache = weakref.WeakValueDictionary()

    def __new__(cls, name):
        if name in _spam_cache:
            return _spam_cache[name]
        else:
            self = super().__new__(cls)
            _spam_cache[name] = self
            return self

    def __init__(self, name):
        self.name = name


class CachedSpamManager:
    def __init__(self):
        self._cache = weakref.WeakValueDictionary()

    def get_spam(self, name):
        if name not in self._cache:
            tmp = Spam3._new(name)
            self._cache[name] = tmp
        else:
            tmp = self._cache[name]
        return tmp


class Spam3:
    def __init__(self, *args, **kwargs):
        raise RuntimeError('Can not instantiate directly')

    @classmethod
    def _new(cls, name):
        self = cls.__new__(cls)
        self.name = name
        return self


def cached_demo():
    a = get_spam('foo')
    b = get_spam('bar')
    c = get_spam('foo')

    print(a is c)

    d = Spam2('a')
    e = Spam2('a')

    print(d is e)

    cache = CachedSpamManager()

    f = cache.get_spam('3')
    g = cache.get_spam('3')
    h = cache.get_spam('4')

    print(f is g)
    print(f is h)


def main():
    cached_demo()


if __name__ == '__main__':
    main()
