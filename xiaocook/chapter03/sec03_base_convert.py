#!/usr/bin/env python
# encoding: utf-8

"""
@description: 进制转化

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec03_base_convert.py
@time: 2016/12/24 22:24
"""

import os


def convert():
    num = 1234
    print(bin(num))
    print(oct(num))
    print(hex(num))

    print(format(num, 'b'))
    print(format(num, 'o'))
    print(format(num, 'x'))

    x = -1234
    print(format(x, 'b'))
    print(format(2 ** 32 + x, 'b'))
    print(format(2 ** 32 + x, 'x'))


def unconvert():
    print(int('4d2', 16))
    print(int('10011010010', 2))


def test_octal():
    print(os.chmod(__file__, 0o755))


def main():
    # convert()
    # unconvert()
    test_octal()


if __name__ == '__main__':
    main()
