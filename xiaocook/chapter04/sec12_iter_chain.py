#!/usr/bin/env python
# encoding: utf-8

"""
@description: 连接多个集合的迭代

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec12_iter_chain.py
@time: 2016/12/25 18:17
"""

from itertools import chain


def multi_collect():
    a = [1, 2, 3, 4]
    b = ['x', 'y', 'z']

    for x in chain(a, b):
        print(x)


def main():
    print("do sth")


if __name__ == '__main__':
    main()
