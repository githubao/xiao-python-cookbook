#!/usr/bin/env python
# encoding: utf-8

"""
@description: 解析xml数据

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec03_xml_parse.py
@time: 2017/1/2 18:58
"""

from urllib.request import urlopen
# from xml.etree.cElementTree import parse
from lxml.etree import parse


def parser():
    u = urlopen('http://planet.python.org/rss20.xml')
    doc = parse(u)

    for item in doc.iterfind('channel/item'):
        title = item.findtext('title')
        date = item.findtext('pubDate')
        link = item.findtext('link')

        print(title)
        print(date)
        print(link)
        break

    e = doc.find('channel/title')
    print(e)
    print(e.tag)
    print(e.text)


def main():
    parser()


if __name__ == '__main__':
    main()
