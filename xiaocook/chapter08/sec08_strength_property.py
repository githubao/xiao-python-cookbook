#!/usr/bin/env python
# encoding: utf-8

"""
@description: 加强property的功能

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec08_strength_property.py
@time: 2017/2/8 19:47
"""


class Person:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._name = value

    @name.deleter
    def name(self):
        raise AttributeError('can not delete attribute')


class SubPerson(Person):
    @Person.name.getter
    # @property
    def name(self):
        print('Getting name')
        return super().name

    @name.setter
    def name(self, value):
        print('Setting name to {}'.format(value))
        super(SubPerson, SubPerson).name.__set__(self, value)

    @name.deleter
    def name(self):
        print('Deleting name')
        super(SubPerson, SubPerson).name.__delete__(self)


def main():
    s = SubPerson('x')
    print(s.name)
    del s.name


if __name__ == '__main__':
    main()
