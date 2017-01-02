#!/usr/bin/env python
# encoding: utf-8

"""
@description: 处理带命名空间的xml

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec07_xml_ns.py
@time: 2017/1/2 20:10
"""

from xml.etree.ElementTree import parse, iterparse

from xiaocook.settings import FILE_PATH

file_name = '{}/demo_ns.xml'.format(FILE_PATH)


def parse_ns():
    doc = parse(file_name)

    print(doc.findtext('author'))
    print(doc.find('content'))
    print(doc.find('content/html'))
    print(doc.find('content/{http://www.w3.org/1999/xhtml}html'))
    print(doc.find(
            'content/{http://www.w3.org/1999/xhtml}html/{http://www.w3.org/1999/xhtml}head/{http://www.w3.org/1999/xhtml}title'))

    ns = XmlNamespaces(html='http://www.w3.org/1999/xhtml')

    print(doc.findtext(ns('content/{html}html')))


class XmlNamespaces():
    def __init__(self, **kwargs):
        self.namespaces = {}
        for name, url in kwargs.items():
            self.register(name, url)

    def register(self, name, url):
        self.namespaces[name] = '{{{}}}'.format(url)

    def __call__(self, path):
        return path.format_map(self.namespaces)


def iterparse_ns():
    for event, elem in iterparse(file_name, ('end', 'start-ns', 'end-ns')):
        print(event, ' ', elem)


def main():
    parse_ns()
    iterparse_ns()


if __name__ == '__main__':
    main()
