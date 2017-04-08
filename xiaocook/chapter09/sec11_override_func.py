#!/usr/bin/env python
# encoding: utf-8

"""
@description: 重载类

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec11_override_func.py
@time: 2017/4/8 16:17
"""


class Spam:
    def bar(self, x: int, y: int):
        print('Bar 1: ', x, y)

    def bar(self, s: str, n: int = 0):
        print('Bar 2: ', s, n)


def override():
    s = Spam()
    s.bar(2, 3)
    s.bar('hello')


def main():
    override()


if __name__ == '__main__':
    main()
