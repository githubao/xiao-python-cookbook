#!/usr/bin/env python
# encoding: utf-8

"""
@description: 顺序迭代合并后的对象

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec14_iter_merged.py
@time: 2016/12/25 21:21
"""

import heapq
from xiaocook.util.settings import FILE_PATH


def iter_merge():
    a = [1, 4, 7, 10]
    b = [2, 5, 6, 11]
    for c in heapq.merge(a, b):
        print(c)


def iter_merge_file():
    with open(FILE_PATH + 'iter_demo_1.txt') as f1, \
            open(FILE_PATH + 'iter_demo_2.txt') as f2, \
            open(FILE_PATH + 'iter_demo_out.txt', 'w') as fw:
        for line in heapq.merge(f1, f2):
            fw.write(line)


def main():
    # iter_merge()
    iter_merge_file()


if __name__ == '__main__':
    main()
