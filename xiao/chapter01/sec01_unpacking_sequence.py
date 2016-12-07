#!/usr/bin/env python
# encoding: utf-8

"""
@description: 解包装列表

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec01_unpacking_sequence.py
@time: 2016/12/6 22:38
"""


def unpack_sequence():
    p = (4, 5)
    (x, y) = p
    print(x)
    print(y)

    data = ['ACME', 50, 91.9, (2012, 12, 31)]
    (name, shares, price, date) = data
    print(name)
    print(date)

    (name, shares, price, (year, mon, day)) = data
    print(name)
    print(year)
    print(mon)
    print(day)

    # err
    # (x, y, z) = p


def main():
    unpack_sequence()


if __name__ == '__main__':
    main()
