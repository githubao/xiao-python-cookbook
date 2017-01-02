#!/usr/bin/env python
# encoding: utf-8

"""
@description: 把字典对象转化为xml

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec05_xml_dict.py
@time: 2017/1/2 19:45
"""

from xml.etree.ElementTree import Element, tostring
from pprint import pprint
from xml.sax.saxutils import escape, unescape


def dic_to_xml(tag, d):
    elem = Element(tag)
    for k, v in d.items():
        child = Element(k)
        child.text = str(v)
        elem.append(child)
    return elem


def to_xml():
    s = {'name': 'GOOG', 'shares': 100, 'price': 490.1}
    e = dic_to_xml('stock', s)
    pprint(tostring(e), indent=4)

    e.set('id', '333')
    print(tostring(e))


def escape_demo():
    e = escape('<span>')
    print(e)
    print(unescape(e))


def main():
    # to_xml()
    escape_demo()


if __name__ == '__main__':
    main()
