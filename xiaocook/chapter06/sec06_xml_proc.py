#!/usr/bin/env python
# encoding: utf-8

"""
@description: xml 处理

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec06_xml_proc.py
@time: 2017/1/2 20:03
"""
from xml.etree.ElementTree import Element, parse
from xiaocook.settings import FILE_PATH

file_name = '{}/pred.xml'.format(FILE_PATH)
new_file_name = '{}/newpred.xml'.format(FILE_PATH)


def proc():
    doc = parse(file_name)
    root = doc.getroot()

    root.remove(root.find('sri'))
    root.remove(root.find('cr'))

    print(root.getchildren().index(root.find('nm')))

    # 在nm后面插入一个新的节点
    e = Element('spam')
    e.text = 'i am new'
    root.insert(2, e)

    doc.write(new_file_name, xml_declaration=True)


def main():
    proc()


if __name__ == '__main__':
    main()
