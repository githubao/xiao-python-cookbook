#!/usr/bin/env python
# encoding: utf-8

"""
@description: 复数的相关运算

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec06_complex.py
@time: 2016/12/24 23:25
"""

import cmath
import numpy as np


def complex_demo():
    a = complex(2, 4)
    b = 3 - 5j
    print(a)
    print(b)

    print(a.real)
    print(a.imag)
    print(a.conjugate())

    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)
    print(abs(a))

    print(cmath.sin(a))
    print(cmath.cos(a))
    print(cmath.exp(a))


def np_complex():
    a = np.array([2 + 3j, 4 + 5j, 6 - 7j, 8 + 9j])
    print(a)
    print(a + 2)
    print(np.sin(a))

    print(cmath.sqrt(-1))


def main():
    # complex_demo()
    np_complex()


if __name__ == '__main__':
    main()
