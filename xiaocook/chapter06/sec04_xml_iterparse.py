#!/usr/bin/env python
# encoding: utf-8

"""
@description: 迭代器处理xml

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec04_xml_iterparse.py
@time: 2017/1/2 19:12
"""

from collections import Counter
from xml.etree.ElementTree import iterparse
from xiaocook.settings import FILE_PATH

file_name = FILE_PATH + "potholes.xml"


def parse_and_remove(filename, path):
    path_parts = path.split('/')
    doc = iterparse(filename, ('start', 'end'))
    next(doc)

    tag_stack = []
    elem_stack = []
    for event, elem in doc:
        if event == 'start':
            tag_stack.append(elem.tag)
            elem_stack.append(elem)
        elif event == 'end':
            if tag_stack == path_parts:
                yield elem
                # 父节点中移除上次已经yield的数据
                elem_stack[-2].remove(elem)
            try:
                tag_stack.pop()
                elem_stack.pop()
            except IndexError:
                pass


def iter_parse():
    potholes_by_zip = Counter()
    data = parse_and_remove(file_name, 'rows/row')
    for pothole in data:
        potholes_by_zip[pothole.findtext('zip')] += 1
    for zipcode, num in potholes_by_zip.most_common():
        print(zipcode, ' ', num)


def main():
    iter_parse()


if __name__ == '__main__':
    main()
