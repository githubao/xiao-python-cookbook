#!/usr/bin/env python
# encoding: utf-8

"""
@description: 迭代器切片

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec07_iter_slice.py
@time: 2016/12/25 17:25
"""

import itertools


def count(n):
    while True:
        yield n
        n += 1


def iter_slice():
    c = count(0)

    for x in itertools.islice(c, 10, 20):
        print(x)


def main():
    iter_slice()


if __name__ == '__main__':
    main()
