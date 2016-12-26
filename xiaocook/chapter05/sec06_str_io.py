#!/usr/bin/env python
# encoding: utf-8

"""
@description: 字符串的io操作

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec06_str_io.py
@time: 2016/12/26 20:47
"""

import io


def str_io():
    s = io.StringIO()
    s.write('Hello World\n')
    print('This is a test', file=s)

    print(s.getvalue())

    t = io.StringIO('Hello World\n')
    print(t.read(6))
    print(t.read())


def bytes_io():
    s = io.BytesIO()
    s.write(b'binary data')
    print(s.getvalue())


def main():
    # str_io()
    bytes_io()


if __name__ == '__main__':
    main()
