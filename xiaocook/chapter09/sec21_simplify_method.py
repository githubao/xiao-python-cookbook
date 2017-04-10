#!/usr/bin/env python
# encoding: utf-8

"""
@description: 简化方法

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec21_simplify_method.py
@time: 2017/4/10 17:28
"""

from functools import partial


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('name must be a string')
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise TypeError('age must be an int')
        self._age = value


def typed_property(name, expected_type):
    storage_name = '_' + str(name)

    @property
    def prop(self):
        return getattr(self, storage_name)

    @prop.setter
    def prop(self, value):
        if not isinstance(value, expected_type):
            raise TypeError('{} must be a {}'.format(name, expected_type))
        setattr(self, storage_name, value)

    return prop


class Person2:
    name = typed_property('name', str)
    age = typed_property('age', int)

    def __init__(self, name, age):
        self.name = name
        self.age = age


String = partial(typed_property, expected_type=str)
Integer = partial(typed_property, expected_type=int)


class Person3:
    name = String('name')
    age = Integer('age')

    def __init__(self, name, age):
        self.name = name
        self.age = age


def run():
    # p = Person('bob', 24)
    p = Person3('bob', '24')


def main():
    run()


if __name__ == '__main__':
    main()
