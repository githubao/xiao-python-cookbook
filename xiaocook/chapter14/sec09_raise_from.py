#!/usr/bin/env python
# encoding: utf-8

"""
@description: 捕获之后抛出新的异常

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec09_raise_from.py
@time: 2017/4/11 21:45
"""


def example():
    try:
        int('N/A')
    except ValueError as e:
        if e.__cause__:
            print('cause: ', e.__cause__)
        raise RuntimeError('A parsing error occurred') from e


def main():
    example()


if __name__ == '__main__':
    main()
