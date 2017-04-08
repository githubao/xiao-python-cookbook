#!/usr/bin/env python
# encoding: utf-8

"""
@description: 自定义控制类的顺序

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec14_ordered_attr.py
@time: 2017/4/8 13:10
"""

from collections import OrderedDict


class Typed:
    _expected_type = type(None)

    def __init__(self, name=None):
        self._name = name

    def __set__(self, instance, value):
        if not isinstance(value, self._expected_type):
            raise TypeError('Expected {}'.format(self._expected_type))
        instance.__dict__[self._name] = value


class Integer(Typed):
    _expected_type = int


class Float(Typed):
    _expected_type = float


class String(Typed):
    _expected_type = str


class NoDupOrderedDict(OrderedDict):
    def __init__(self, clsname, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.clsname = clsname

    def __setitem__(self, key, value):
        if key in self:
            raise TypeError('{} already defined in {}'.format(key, self.clsname))

        super().__setitem__(key, value)


class OrderedMeta(type):
    def __new__(cls, clsname, bases, clsdict):
        d = dict(clsdict)
        order = []
        for name, value in clsdict.items():
            if isinstance(value, Typed):
                value._name = name
                order.append(name)
        d['_order'] = order
        return type.__new__(cls, clsname, bases, d)

    @classmethod
    def __prepare__(cls, clsname, bases):
        # return OrderedDict()
        return NoDupOrderedDict(clsname)


class Structure(metaclass=OrderedMeta):
    def as_csv(self):
        return '.'.join(str(getattr(self, name)) for name in self._order)

    def Spam(self):
        pass

    def Spam(self):
        pass


class Stock(Structure):
    name = String()
    shares = Integer()
    price = Float()

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price


def run():
    s = Stock('GOOG', 100, 490.1)
    print(s.as_csv())


def main():
    run()


if __name__ == '__main__':
    main()
