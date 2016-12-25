#!/usr/bin/env python
# encoding: utf-8

"""
@description: 矩阵运算

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec10_matrix.py
@time: 2016/12/25 12:49
"""

import numpy as np
from numpy import linalg


def matrix():
    m = np.matrix([[1, -2, 3], [0, 4, 5], [7, 8, -9]])
    print(m)

    # 转置
    print(m.T)

    # 求逆
    print(m.I)

    v = np.matrix([[2], [3], [4]])

    print(v)

    print(m * v)

    # 行列式
    print(linalg.det(m))

    # 特征值
    print(linalg.eigvals(m))

    # 求解
    x = linalg.solve(m, v)
    print(x)

    print(m * x == v)


def main():
    matrix()


if __name__ == '__main__':
    main()
