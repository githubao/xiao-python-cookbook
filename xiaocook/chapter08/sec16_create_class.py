#!/usr/bin/env python
# encoding: utf-8

"""
@description: 创建类的多种方法

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec16_create_class.py
@time: 2017/2/28 21:48
"""

import time


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def today(cls):
        t = time.localtime()
        return cls(t.tm_year, t.tm_mon, t.tm_mday)

    def __str__(self):
        return '{}'.format(self.__dict__)


def demo():
    a = Date(2017, 2, 28)
    print(a)
    b = Date.today()
    print(b)


def main():
    demo()


if __name__ == '__main__':
    main()
