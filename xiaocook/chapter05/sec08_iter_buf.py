#!/usr/bin/env python
# encoding: utf-8

"""
@description: 固定的长度的读取数据

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec08_iter_buf.py
@time: 2016/12/26 21:13
"""

from functools import partial
from xiaocook.util.settings import FILE_PATH

FILE_NAME = FILE_PATH + 'Documentation.html'

RECORD_SIZE = 32


def part():
    with open(FILE_NAME, 'r') as f:
        records = iter(partial(f.read, RECORD_SIZE), '')
        for r in records:
            print(r)
            print("*" * 20)


def main():
    part()


if __name__ == '__main__':
    main()
