#!/usr/bin/env python
# encoding: utf-8

"""
@description: print 的其他参数

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec03_print_sep.py
@time: 2016/12/25 22:06
"""


def print_sep():
    print('ACME', 50, 91.5)
    print('ACME', 50, 91.5, sep=',')
    print('ACME', 50, 91.5, sep=',', end='!!\n')

    for i in range(5):
        print(i)

    for i in range(5):
        print(i, end=' ')

    row = ('ACME', 50, 91.5)
    print(*row, sep=',')


def main():
    print_sep()


if __name__ == '__main__':
    main()
