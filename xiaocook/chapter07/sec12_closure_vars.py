#!/usr/bin/env python
# encoding: utf-8

"""
@description: 访问闭包中的变量

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec12_closure_vars.py
@time: 2017/1/8 15:39
"""

import sys
from timeit import timeit


def sample():
    n = 0

    def func():
        print('n=', n)

    def get_n():
        return n

    def set_n(value):
        nonlocal n
        n = value

    func.get_n = get_n
    func.set_n = set_n

    return func


class ClosureInstance():
    def __init__(self, locals=None):
        if locals is None:
            locals = sys._getframe(1).f_locals

        self.__dict__.update((k, v) for k, v in locals.items() if callable(v))

    def __len__(self):
        return self.__dict__['__len__']()


def Stack():
    items = []

    def push(item):
        items.append(item)

    def pop():
        return items.pop()

    def __len__():
        return len(items)

    return ClosureInstance()


def closure_var_demo():
    f = sample()
    print(f)
    f()

    f.set_n(6)
    f()
    print(f.get_n())


def closure_var_demo2():
    s = Stack()
    print(s)

    s.push(10)
    s.push('jjj')
    print(s.pop())
    print(s.pop())


def efficiency():
    print(timeit('s.push(1);s.pop()', 'from __main__ import s'))


def main():
    # closure_var_demo()
    # closure_var_demo2()
    efficiency()


if __name__ == '__main__':
    s = Stack()

    main()
