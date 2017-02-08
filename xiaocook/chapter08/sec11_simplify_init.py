#!/usr/bin/env python
# encoding: utf-8

"""
@description:

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec11_simplify_init.py
@time: 2017/2/8 20:13
"""

import math


class Structure1:
    _fields = []

    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError('Expected {} arguments'.format(len(self._fields)))
        for name, value in zip(self._fields, args):
            setattr(self, name, value)


# 关键字参数
class Structure2:
    _fields = []

    def __init__(self, *args, **kwargs):
        if len(args) > len(self._fields):
            raise TypeError('Expected {} arguments'.format(len(self._fields)))
        for name, value in zip(self._fields, args):
            setattr(self, name, value)

        for name in self._fields[len(args):]:
            setattr(self, name, kwargs.pop(name))

        if kwargs:
            raise TypeError('Invalid argument(s)'.format(','.join(kwargs)))


# 指定类别
class Structure3:
    _fields = []

    def __init__(self, *args, **kwargs):
        if len(args) != len(self._fields):
            raise TypeError('Expected {} arguments'.format(len(self._fields)))
        for name, value in zip(self._fields, args):
            setattr(self, name, value)

        extra_args = kwargs.keys() - self._fields
        for name in extra_args:
            setattr(self, name, kwargs.pop(name))

        if kwargs:
            raise TypeError('Invalid argument(s)'.format(','.join(kwargs)))


class Stock(Structure1):
    _fields = ['name', 'shares', 'price']


class Point(Structure2):
    _fields = ['x', 'y']


class Point3(Structure3):
    _fields = ['x', 'y']


def demo1():
    s = Stock(1, 2, 3)
    p = Point(1, 2)
    print(s.name)
    print(p.x)

    p2 = Point(1, y=2)
    print(p2.x)
    print(p2.y)

    p3 = Point3(1, 2, z=3)
    print(p3.z)


def main():
    demo1()


if __name__ == '__main__':
    main()
