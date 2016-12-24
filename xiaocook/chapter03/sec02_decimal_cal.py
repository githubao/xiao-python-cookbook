#!/usr/bin/env python
# encoding: utf-8

"""
@description: 精确的浮点数计算模块

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec02_decimal_cal.py
@time: 2016/12/24 19:34
"""

from decimal import Decimal, localcontext
import math


def float_defect():
    a = 4.2
    b = 2.1
    print(a + b)
    print((a + b) == 6.3)


def using_decimal():
    a = Decimal('4.2')
    b = Decimal('2.1')
    print(a + b)
    print((a + b) == Decimal('6.3'))


def decimal_cal():
    a = Decimal('1.3')
    b = Decimal('1.7')
    print(a / b)

    with localcontext() as ctx:
        ctx.prec = 3
        print(a / b)

        ctx.prec = 50
        print(a / b)


def big_num_cal():
    num = [1.23e+18, 1, -1.23e+18]
    print(sum(num))

    print(math.fsum(num))


def main():
    # float_defect()
    # using_decimal()
    # decimal_cal()
    big_num_cal()


if __name__ == '__main__':
    main()
