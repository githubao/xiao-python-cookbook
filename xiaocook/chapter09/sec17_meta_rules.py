#!/usr/bin/env python
# encoding: utf-8

"""
@description: 强制遵守一些编程规约

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec17_meta_rules.py
@time: 2017/4/8 13:49
"""
from inspect import signature
import logging


class MyMeta(type):
    def __new__(cls, clsname, bases, clsdict):
        return super().__new__(cls, clsname, bases, clsdict)

    def __init__(self, clsname, bases, clsdict):
        super().__init__(clsname, bases, clsdict)


class NoMixedCaseMeta(type):
    def __new__(cls, clsname, bases, clsdict):
        for name in clsdict:
            if name.lower() != name:
                raise TypeError('Bad attribute name: ', name)

        return super().__new__(cls, clsname, bases, clsdict)


class MatchSignaturesMeta(type):
    def __init__(self, clsname, bases, clsdict):
        super().__init__(clsname, bases, clsdict)

        sup = super(self, self)
        for name, value in clsdict.items():
            if name.startswith('_'):
                continue
            prev_dfn = getattr(sup, name, None)
            if prev_dfn:
                prev_sig = signature(prev_dfn)
                val_sig = signature(value)
                if prev_sig != val_sig:
                    logging.warning('Signature mismatch in {}, {} != {}'.format(
                            value.__qualname__, prev_sig, val_sig
                    ))


# class Root(metaclass=NoMixedCaseMeta):
class Root(metaclass=MatchSignaturesMeta):
    pass


class A(Root):
    def foo_bar(self):
        pass


class B(Root):
    def fooBar(self):
        pass


class C(Root):
    def foo(self, a, b):
        pass


class D(C):
    def foo(self, x, y):
        pass


def run():
    # a = A()
    c = C()


def main():
    run()


if __name__ == '__main__':
    main()
