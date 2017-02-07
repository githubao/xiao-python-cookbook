#!/usr/bin/env python
# encoding: utf-8

"""
@description: 使用super 调用父类方法

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec07_use_super.py
@time: 2017/2/7 20:04
"""


class A:
    def spam(self):
        print('A.spam')


class B(A):
    def spam(self):
        print('B.spam')
        super().spam()


# '__getattr__' 对应属性不存在时，如果处理
# getattr 就是用来获取属性的
# __getattribute__ 每次任何条件下，无条件被确定调用

class Proxy:
    def __init__(self, obj):
        self._obj = obj

    def __getattr__(self, item):
        return getattr(self._obj, item)

    def __setattr__(self, key, value):
        if key.startswith('_'):
            super().__setattr__(key, value)
        else:
            setattr(self._obj, key, value)


# 多继承的原理，使用super() 而不要直接使用’父类名‘

class M:
    def spam(self):
        print('M.spam')
        super().spam()


class N:
    def spam(self):
        print('N.spam')


class L(M, N):
    def spam(self):
        print('L.spam')
        super().spam()


def main():
    # b = B()
    b = L()
    b.spam()
    print(L.__mro__)


if __name__ == '__main__':
    main()
