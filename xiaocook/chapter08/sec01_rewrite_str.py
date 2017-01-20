#!/usr/bin/env python
# encoding: utf-8

"""
@description: 重写str方法

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec01_rewrite_str.py
@time: 2017/1/8 16:01
"""


class Pair():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Pair({self.x!r}, {self.y!r})'.format(self=self)

    def __str__(self):
        return '({self.x!s}, {self.y!s})'.format(self=self)


def obj_str_demo():
    pair = Pair(3, 4)
    print(repr(pair))
    print(str(pair))

def obj_str_demo2():
    f = open(__file__)
    print(f)

def main():
    # obj_str_demo()
    obj_str_demo2()


if __name__ == '__main__':
    main()
