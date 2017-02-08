#!/usr/bin/env python
# encoding: utf-8

"""
@description: 重写 get set delete

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec09_property_descriptor.py
@time: 2017/2/8 19:33
"""


class Integer:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError('Expected an int')
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]


class Point:
    x = Integer('x')
    y = Integer('y')

    def __init__(self, x, y):
        self.x = x
        self.y = y

# 实现更复杂的类型检查
class Typed:
    def __init__(self, name,expected_type):
        self.name = name
        self.expected_type =expected_type

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError('Expected {}'.format(self.expected_type))
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]


def typeassert(**kwargs):
    def decorate(cls):
        for name,expected_type in kwargs.items():
            setattr(cls,name,Typed(name,expected_type))
        return cls
    return decorate

@typeassert(name=str,share=int,price=float)
class Stock:
    def __init__(self,name,share,price):
        self.name = name
        self.share = share
        self.price = price





def demo1():
    p1 = Point(2, 3)
    p2 = Point(2, 3.5)


def main():
    demo1()


if __name__ == '__main__':
    main()
