#!/usr/bin/env python
# encoding: utf-8

"""
@description: 强制参数签名

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec16_force_args.py
@time: 2017/4/8 13:33
"""

from inspect import Signature, Parameter
import inspect


def params(*args, **kwargs):
    params = [Parameter('x', Parameter.POSITIONAL_OR_KEYWORD),
              Parameter('y', Parameter.POSITIONAL_OR_KEYWORD, default=42),
              Parameter('z', Parameter.KEYWORD_ONLY, default=None)
              ]

    sig = Signature(parameters=params)
    # print(sig)

    bound_values = sig.bind(*args, **kwargs)
    for name, value in bound_values.arguments.items():
        print(name, value)


def demo():
    params(1, 2)
    params(x=1, z=3)
    params(1, 2, 3, 4)


def make_sig(*names):
    params = [Parameter(name, Parameter.POSITIONAL_OR_KEYWORD)
              for name in names]
    return Signature(parameters=params)


class Structure:
    __signature__ = make_sig()

    def __init__(self, *args, **kwargs):
        bound_values = self.__signature__.bind(*args, **kwargs)
        for name, value in bound_values.arguments.items():
            setattr(self, name, value)


class Stock(Structure):
    __signature__ = make_sig('name', 'shares', 'price')


class Point(Structure):
    __signature__ = make_sig('x', 'y')


def demo2():
    print(inspect.signature(Stock))
    print(inspect.signature(Stock2))


class StructureMeta(type):
    def __new__(cls, clsname, bases, clsdict):
        clsdict['__signature__'] = make_sig(*clsdict.get('_fields', []))
        return super().__new__(cls, clsname, bases, clsdict)


class Structure2(metaclass=StructureMeta):
    _fields = []

    def __init__(self, *args, **kwargs):
        bound_values = self.__signature__.bind(*args, **kwargs)
        for name, value in bound_values.arguments.items():
            setattr(self, name, value)


class Stock2(Structure2):
    _fields = ['a', 'b', 'c']


def main():
    # demo()
    demo2()


if __name__ == '__main__':
    main()
