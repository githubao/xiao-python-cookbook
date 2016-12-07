#!/usr/bin/env python
# encoding: utf-8

"""
@description:一个键，对应多个值的字典

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec06_defaultdict_multi_dict.py
@time: 2016/12/7 20:37
"""

from collections import defaultdict

d1 = {
    'a': [1, 2, 3],
    'b': [4, 5],
}

d2 = {
    'a': {1, 2, 3},
    'b': {4, 5},
}


def default_dict():
    print(d1)
    print(d2)

    d = defaultdict(list)
    d['a'].append(1)
    d['a'].append(2)
    d['b'].append(4)
    print(d)

    d = defaultdict(set)
    d['a'].add(1)
    d['a'].add(2)
    d['b'].add(4)
    print(d)


def main():
    default_dict()


if __name__ == '__main__':
    main()
