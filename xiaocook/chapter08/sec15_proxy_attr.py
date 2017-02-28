#!/usr/bin/env python
# encoding: utf-8

"""
@description: 实现代理属性的访问

__getattr__ 对‘__’开头的方法并不适用

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec15_proxy_attr.py
@time: 2017/2/28 21:37
"""


class A:
    def spam(self, x):
        pass

    def foo(self):
        pass


class B1:
    def __init__(self):
        self._a = A()

    def spam(self, x):
        return self._a.spam(x)

    def foo(self):
        return self._a.foo()

    def bar(self):
        pass


class B2:
    def __init__(self):
        self._a = A()

    def __getattr__(self, item):
        return getattr(self._a, item)

    def bar(self):
        pass


class Proxy:
    def __init__(self, obj):
        self._obj = obj

    def __getattr__(self, item):
        print('get attr: ', item)
        return getattr(self._obj, item)

    def __setattr__(self, key, value):
        if key.startswith('_'):
            super().__setattr__(key, value)
        else:
            print('set attr: ', key, value)
            setattr(self._obj, key, value)

    def __delattr__(self, item):
        if item.startswith('_'):
            super().__delattr__(item)
        else:
            print('del attr: ', item)
            delattr(self._obj, item)


class Spam():
    def __init__(self, x):
        self.x = x

    def bar(self, y):
        print('spam.bar: ', self.x, y)


def demo():
    s = Spam(2)
    p = Proxy(s)

    print(p.x)
    p.bar(3)


def main():
    demo()


if __name__ == '__main__':
    main()
