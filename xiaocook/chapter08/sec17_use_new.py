#!/usr/bin/env python
# encoding: utf-8

"""
@description: 使用new方法创建实例

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec17_use_new.py
@time: 2017/2/28 21:57
"""

import time


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        return '{}'.format(self.__dict__)

    @classmethod
    def today(cls):
        d = cls.__new__(cls)
        t = time.localtime()
        d.year = t.tm_year
        return d


def initialize(d):
    data = {'year': 2012, 'month': 8, 'day': 29}
    for key, value in data.items():
        setattr(d, key, value)


def demo():
    d = Date.__new__(Date)
    print(d)
    initialize(d)
    print(d)


def demo2():
    d = Date.today()
    print(d)


def main():
    # demo()
    demo2()


if __name__ == '__main__':
    main()
