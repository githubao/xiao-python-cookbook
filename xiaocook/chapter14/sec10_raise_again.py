#!/usr/bin/env python
# encoding: utf-8

"""
@description: 捕获之后重新抛出

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec10_raise_again.py
@time: 2017/4/11 21:48
"""


def example():
    try:
        int('q')
    except ValueError as e:
        print('err occur exact here!')
        raise


def main():
    example()


if __name__ == '__main__':
    main()
