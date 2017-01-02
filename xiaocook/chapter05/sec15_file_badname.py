#!/usr/bin/env python
# encoding: utf-8

"""
@description: 处理异常的文件名

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec15_file_badname.py
@time: 2017/1/2 14:44
"""

import sys


def bad_name(filename):
    return repr(filename)[1:-1]


def bad_name2(filename):
    temp = filename.encode(sys.getfilesystemencoding(), errors='surrogateescape')
    return temp.decode('latin-1')


def process_file():
    # name = 'bäd.txt'
    name = 'b\udce4d.txt'
    try:
        print(name)
    except UnicodeEncodeError:
        print('unicode err')
        print(bad_name(name))
        print(bad_name2(name))


def main():
    process_file()


if __name__ == '__main__':
    main()
