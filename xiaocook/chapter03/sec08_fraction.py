#!/usr/bin/env python
# encoding: utf-8

"""
@description: 分数计算

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec08_fraction.py
@time: 2016/12/25 0:03
"""

from fractions import Fraction


def fractions_demo():
    a = Fraction(5, 4)
    b = Fraction(7, 16)
    print(a + b)
    print(a * b)

    c = a * b
    print(c.numerator)
    print(c.denominator)
    print(float(c))

    print(c.limit_denominator(8))

    x = 3.75
    y = Fraction(*x.as_integer_ratio())
    print(y)


def main():
    fractions_demo()


if __name__ == '__main__':
    main()
