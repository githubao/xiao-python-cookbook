#!/usr/bin/env python
# encoding: utf-8

"""
@description: 通过字符串调用方法

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec20_str_call.py
@time: 2017/3/1 20:31
"""

import math
import operator


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Point({!r:},{!r:})'.format(self.x, self.y)

    def distance(self, x, y):
        return math.hypot(self.x - x, self.y - y)


points = [
    Point(1, 2),
    Point(3, 0),
    Point(10, -3),
    Point(-5, -7),
    Point(-1, 8),
    Point(3, 2)
]


def method_call():
    p = Point(2, 3)
    d = getattr(p, 'distance')(0, 0)
    print(d)

    d2 = operator.methodcaller('distance', 0, 0)(p)
    print(d2)

    print(sorted(points, key=operator.methodcaller('distance', 0, 0)))


def main():
    method_call()


if __name__ == '__main__':
    main()
