#!/usr/bin/env python
# encoding: utf-8

"""
@description: 类装饰器

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec08_class_wrap.py
@time: 2017/4/7 23:18
"""

from functools import wraps


class A:
    def decorator1(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('decorator 1')
            return func(*args, **kwargs)

        return wrapper

    @classmethod
    def decorator2(cls, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('decorator 2')
            return func(*args, **kwargs)

        return wrapper


a = A()


@a.decorator1
def spam():
    pass


@A.decorator2
def grok():
    pass


class Person:
    _first_name = 'anno'

    first_name = property()

    @first_name.getter
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._first_name = value


class B(A):
    @A.decorator2
    def bar(self):
        pass


def main():
    spam()
    grok()


if __name__ == '__main__':
    main()
