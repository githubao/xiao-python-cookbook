#!/usr/bin/env python
# encoding: utf-8

"""
@description: 过滤列表

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec16_filter_list.py
@time: 2016/12/9 20:00
"""

from itertools import compress

mylist = [1, 4, -5, 10, -7, 2, 3, -1]
values = ['1', '2', '-3', '-', '4', 'N/A', '5']

addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK'
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE'
]
counts = [0, 3, 10, 4, 1, 7, 6, 1]


def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False


def filter_list():
    print([n for n in mylist if n > 0])
    pos = (n for n in mylist if n > 0)
    for item in pos:
        print(item)


def filter_func():
    ivals = list(filter(is_int, values))
    print(ivals)


def filter_demo():
    clip_neg = [n if n > 0 else 0 for n in mylist]
    clip_pos = [n if n < 0 else 0 for n in mylist]
    print(clip_neg)
    print(clip_pos)

    more5 = [n > 5 for n in counts]
    print(more5)
    print(list(compress(addresses, more5)))


def main():
    # filter_list()
    # filter_func()
    filter_demo()


if __name__ == '__main__':
    main()
