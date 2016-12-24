#!/usr/bin/env python
# encoding: utf-8

"""
@description: numpy

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec09_numpy.py
@time: 2016/12/25 0:08
"""

import numpy as np


def f(x):
    return 3 * x ** 2 - 2 * x + 7


def numpy_demo():
    ax = np.array([1, 2, 3, 4])
    bx = np.array([5, 6, 7, 8])

    print(ax + 10)
    print(ax + bx)
    print(ax * 2)
    print(ax * bx)

    print(f(ax))
    print(np.sqrt(ax))
    print(np.sin(ax))


def numpy_grid():
    grid = np.zeros(shape=(10000, 10000), dtype=float)
    print(grid)

    print(grid + 10)
    print(np.sin(grid))


def numpy_index():
    a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    print(a)
    print(a[1])
    print(a[:, 1])
    print(a[1:3, 1:3])

    print(a + [100, 101, 102, 103])
    print(np.where(a < 10, a, 10))


def main():
    # numpy_demo()
    # numpy_grid()
    numpy_index()


if __name__ == '__main__':
    main()
