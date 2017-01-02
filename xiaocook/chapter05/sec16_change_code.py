#!/usr/bin/env python
# encoding: utf-8

"""
@description: 改变文件编码

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec16_change_code.py
@time: 2017/1/2 14:56
"""

import urllib.request
import io
import sys


def change():
    url = urllib.request.urlopen('http://www.python.org')
    f = io.TextIOWrapper(url, encoding='utf-8')
    print(f.read())


def terminal():
    print(sys.stdout.encoding)

    sys.stdout = io.TextIOWrapper(sys.__stdout__.detach(), encoding='latin-1')

    print(sys.stdout.encoding)


def codecs():
    f = open(__file__, 'r',encoding='utf-8')
    print(f)
    print(f.buffer)
    print(f.buffer.raw)


def io_err():
    sys.stdout = io.TextIOWrapper(sys.__stdout__.detach(),encoding='ascii',errors='xmlcharrefreplace')
    print('Jalape\u00f1o')


def main():
    # terminal()
    # codecs()
    io_err()


if __name__ == '__main__':
    main()
