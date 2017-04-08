#!/usr/bin/env python
# encoding: utf-8

"""
@description: 用装饰器实现修改类的功能

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec12_decorate_func.py
@time: 2017/4/8 12:05
"""


def log_getattribute(cls):
    orig_getattribute = cls.__getattribute__

    def new_getattribute(self, name):
        print('getting: ', name)
        return orig_getattribute(self, name)

    cls.__getattribute__ = new_getattribute
    return cls


class LoggedGetAttribute:
    def __getattribute__(self, item):
        print('getting: ', item)
        return super().__getattribute__(item)


# @log_getattribute
class A(LoggedGetAttribute):
    def __init__(self, x):
        self.x = x

    def spam(self):
        pass


def run():
    a = A(42)
    print(a.x)

    print(a.spam())


def main():
    run()


if __name__ == '__main__':
    main()
