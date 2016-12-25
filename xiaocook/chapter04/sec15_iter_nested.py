#!/usr/bin/env python
# encoding: utf-8

"""
@description: 处理迭代的序列

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec15_iter_nested.py
@time: 2016/12/25 21:16
"""

from collections import Iterable


def flatten(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from flatten(x)
        else:
            yield x


def nest():
    items = [1, 2, [3, 4, [5, 6], 7], 8]
    for x in flatten(items):
        print(x)

    items = ['Dave', 'Paula', ['Thomas', 'Lewis']]
    for x in flatten(items):
        print(x)

def main():
    nest()


if __name__ == '__main__':
    main()
