#!/usr/bin/env python
# encoding: utf-8

"""
@description: 排列组合

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec09_perm_comb.py
@time: 2016/12/25 17:52
"""

from itertools import permutations, combinations, combinations_with_replacement


def perm_and_comb():
    items = ['a', 'b', 'c']
    for p in permutations(items):
        print(p)

    print('*' * 20)
    for p in permutations(items, 2):
        print(p)

    print('*' * 20)
    for c in combinations(items, 2):
        print(c)

    print('*' * 20)
    for c in combinations_with_replacement(items, 3):
        print(c)


def main():
    perm_and_comb()


if __name__ == '__main__':
    main()
