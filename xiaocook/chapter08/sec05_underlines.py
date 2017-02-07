#!/usr/bin/env python
# encoding: utf-8

"""
@description: python 下划线约定

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec05_underlines.py
@time: 2017/2/7 19:42
"""


class A:
    def __init__(self):
        self._internal = 0
        self.public = 1

    def public_method(self):
        pass

    def _internal_method(self):
        pass


# 双下划线的名字不会被继承
class B:
    def __init__(self):
        self.__private = 0

    def __private_method(self):
        pass


class C(A, B):
    pass


def main():
    c = C()
    print(c)


if __name__ == '__main__':
    main()
