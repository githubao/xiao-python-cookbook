#!/usr/bin/env python
# encoding: utf-8

"""
@description: 属性装饰器

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec06_property_decro.py
@time: 2017/2/7 19:48
"""


class Person:
    def __init__(self, first_name):
        self.first_name = first_name

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._first_name = value

    @first_name.deleter
    def first_name(self):
        raise AttributeError('can not delete attribute')


class Person2:
    def __init__(self, first_name):
        self.set_first_name(first_name)

    def get_first_name(self):
        return self._first_name

    def set_first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._first_name = value

    def del_first_name(self):
        raise AttributeError('can not delete attribute')

    first_name = property(get_first_name, set_first_name, del_first_name)


import math

# 把方法转变为属性调用
class Circle():
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius ** 2


def main2():
    c = Circle(2)
    # print(c.area())
    print(c.area)


def main1():
    a = Person2('a')
    print(a.first_name)

    # a.first_name = 43
    del a.first_name


def main():
    # main1()
    main2()


if __name__ == '__main__':
    main()
