#!/usr/bin/env python
# encoding: utf-8

"""
@description: 使用元类控制实例的创建

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec13_metaclass.py
@time: 2017/4/8 12:14
"""

import weakref


class NoInstances(type):
    def __call__(self, *args, **kwargs):
        raise TypeError('Can not instantiate directly')


class Spam(metaclass=NoInstances):
    @staticmethod
    def grok(x):
        print('Spam grok')


def run():
    Spam.grok(42)
    s = Spam()


class Singleton(type):
    def __init__(self, what, *args, **kwargs):
        super().__init__(what)
        self.__instance = None

    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instance = super.__call__(*args, **kwargs)
            return self.__instance
        else:
            return self.__instance


class Spam2(metaclass=Singleton):
    def __init__(self):
        print('Creating Spam')


def run2():
    a = Spam2()
    b = Spam2()

    print(a is b)


class Cached(type):
    def __init__(self, what, *args, **kwargs):
        super().__init__(what)
        # self.__cache = weakref.WeakKeyDictionary()
        self.__cache = {}

    def __call__(self, *args, **kwargs):
        if args in self.__cache:
            return self.__cache[args]
        else:
            obj = super().__call__(*args)
            self.__cache[args] = obj
            return obj


class Spam3(metaclass=Cached):
    def __init__(self, name):
        print('Creating Spam({!r})'.format(name))
        self.name = name


def run3():
    a = Spam3('a')
    b = Spam3('b')
    c = Spam3('a')

    print(a is b)
    print(a is c)


def main():
    # run()
    # run2()
    run3()


if __name__ == '__main__':
    main()
