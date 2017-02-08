#!/usr/bin/env python
# encoding: utf-8

"""
@description: 属性延迟计算

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec10_lazy_property.py
@time: 2017/2/8 19:59
"""

import math

class lazyproperty:
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            value = self.func(instance)
            setattr(instance, self.func.__name__, value)
            return value


def lazyproperty2(func):
    name = '_lazy_'+func.__name__

    @property
    def lazy(self):
        if hasattr(self,name):
            return getattr(self,name)
        else:
            value = func(self)
            setattr(self,name,value)
            return value

    return lazy


class Circle():
    def __init__(self, radius):
        self.radius = radius

    @lazyproperty2
    def area(self):
        print('computer area')
        return math.pi * self.radius ** 2


def main():
    c = Circle(4)
    print(vars(c))
    print(c.area)
    print(vars(c))
    print(c.area)
    print(vars(c))


if __name__ == '__main__':
    main()
