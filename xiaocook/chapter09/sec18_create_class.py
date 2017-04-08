#!/usr/bin/env python
# encoding: utf-8

"""
@description: 用代码直接创建类

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec18_create_class.py
@time: 2017/4/8 14:36
"""

import types
import collections

import operator
import types
import sys


class Base(type):
    @classmethod
    def __prepare__(cls, name, bases, *, debug=False, typecheck=False):
        pass
        return super().__prepare__(name, bases)

    def __new__(cls, name, bases, ns, *, debug=False, typecheck=False):
        pass
        return super().__new__(cls, name, bases, ns)

    def __init__(self, name, bases, ns, *, debug=False, typecheck=False):
        pass
        super().__init__(name, bases, ns)


def __init__(self, name, shares, price):
    self.name = name
    self.shares = shares
    self.price = price


def cost(self):
    return self.shares * self.price


cls_dict = {
    '__init__': __init__,
    'cost': cost,
}

Stock = types.new_class('Stock', (), {}, lambda ns: ns.update(cls_dict))
Stock.__module__ = __name__


def run():
    s = Stock('ACME', 50, 91.1)
    print(s.cost())


class Spam2(metaclass=Base, debug=True, typecheck=False):
    pass


# 定义新的类
Spam3 = types.new_class('Spam3', (), {'metaclass': Base, 'debug': True, 'typecheck': False},
                        lambda ns: ns.update(cls_dict))

Stock2 = collections.namedtuple('Stock2', ['name', 'shares', 'price'])


def run2():
    print(Stock2)


def my_namedtuple(classname, fieldnames):
    cls_dict = {name: property(operator.itemgetter(n)) for n, name in enumerate(fieldnames)}

    def __new__(cls, *args):
        if len(args) != len(fieldnames):
            raise TypeError('Expected {} arguments'.format(len(fieldnames)))

        return tuple.__new__(cls, args)

    cls_dict['__new__'] = __new__

    cls = types.new_class(classname, (tuple,), {}, lambda ns: ns.update(cls_dict))

    cls.__module__ = sys._getframe(1).f_globals['__name__']
    return cls


def run3():
    Point = my_namedtuple('Point', ('x', 'y'))
    p = Point(4, 5)
    print(p.x)


metaclass, kwargs, ns = types.prepare_class('Stock', (), {'metaclass': type})



def main():
    # run()
    # run2()
    run3()


if __name__ == '__main__':
    main()
