#!/usr/bin/env python
# encoding: utf-8

"""
@description: 固定参数

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec07_fix_args.py
@time: 2017/1/7 20:10
"""

from functools import partial
import math


def spam(a, b, c, d):
    print(a, b, c, d)


def partial_demo():
    s1 = partial(spam, 1)
    s1(2, 3, 4)

    s2 = partial(spam, d=4)
    s2(1, 2, 3)

    s3 = partial(spam, 1, d=4)
    s3(2, 3)


points = [(1, 2), (3, 4), (5, 6), (7, 8)]


def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2

    return math.hypot(x2 - x1, y2 - y1)


# 用于微调函数参数
def partial_demo2():
    pt = (4, 3)

    points.sort(key=partial(distance, pt))
    print(points)


def main():
    # partial_demo()
    partial_demo2()


if __name__ == '__main__':
    main()
