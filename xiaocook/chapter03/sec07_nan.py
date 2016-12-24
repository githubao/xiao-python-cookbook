#!/usr/bin/env python
# encoding: utf-8

"""
@description: nan inf

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec07_nan.py
@time: 2016/12/24 23:56
"""

import math


def test_nan():
    a = float('inf')
    b = float('-inf')
    c = float('nan')
    print(a)
    print(b)
    print(c)

    print(math.isinf(a))
    print(math.isnan(c))


def nan_op():
    a = float('inf')
    b = float('-inf')

    print(a + 45)
    print(b * 10)
    print(10 / a)

    print(a / a)
    print(a + b)

    c = float('nan')
    d = float('nan')

    print(c + 23)
    print(c / 2)
    print(c * 2)
    print(math.sqrt(c))

    print(c == d)
    print(c is d)

    print(math.isnan(c))


def main():
    # test_nan()
    nan_op()


if __name__ == '__main__':
    main()
