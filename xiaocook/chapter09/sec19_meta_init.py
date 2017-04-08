#!/usr/bin/env python
# encoding: utf-8

"""
@description: 自定义元类的初始化

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec19_meta_init.py
@time: 2017/4/8 15:50
"""

import operator


class StructTupleMeta(type):
    def __init__(cls, what, *args, **kwargs):
        super().__init__(what)
        for n, name in enumerate(cls._fields):
            setattr(cls, name, property(operator.itemgetter(n)))


class StructTuple(tuple, metaclass=StructTupleMeta):
    _fields = []

    def __new__(cls, *args):
        if len(args) != len(cls._fields):
            raise ValueError('{} arguments required'.format(len(cls._fields)))

        return super().__new__(cls, args)


class Stock(StructTuple):
    _fields = ['name', 'shares', 'price']


class Point(StructTuple):
    _fields = ['x', 'y']


def main():
    p = Point(3, 4)
    print(p.x)

    p.x = 5


if __name__ == '__main__':
    main()
