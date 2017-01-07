#!/usr/bin/env python
# encoding: utf-8

"""
@description: 函数默认参数

1，
默认参数仅在被定义的时候，赋值一次
2，
不要使用可变对象作为函数默认参数
3，
可变对象使用b is None判断，而不是 not b(长度为0，空元组，空字符串都为真)

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec05_default_args.py
@time: 2017/1/7 19:47
"""


def spam(a, b=42):
    print(a, b)


def spam2(a, b=None):
    if b is None:
        b = []


_no_value = object()


def spam3(a, b=_no_value):
    if b is _no_value:
        print('No b value supplied')
    print(b)


def default_args():
    spam(1)
    spam(1, 2)

    spam3(1)
    spam3(1, 2)
    spam3(1, None)


def main():
    default_args()


if __name__ == '__main__':
    main()
