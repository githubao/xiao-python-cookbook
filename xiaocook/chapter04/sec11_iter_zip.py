#!/usr/bin/env python
# encoding: utf-8

"""
@description: 同时迭代多个序列

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec11_iter_zip.py
@time: 2016/12/25 18:12
"""

from itertools import zip_longest


def iter_many():
    xpts = [1, 5, 4, 2, 10]
    ypts = [101, 78, 37, 15, 62, 99]
    for x, y in zip(xpts, ypts):
        print(x, y)

    print('*' * 20)
    for x, y in zip_longest(xpts, ypts):
        print(x, y)

    print('*' * 20)
    for x, y in zip_longest(xpts, ypts, fillvalue=0):
        print(x, y)


def zip_to_dict():
    headers = ['name', 'shares', 'price']
    values = ['ACME', 100, 490.1]

    s = dict(zip(headers, values))
    print(s)


def main():
    # iter_many()
    zip_to_dict()


if __name__ == '__main__':
    main()
