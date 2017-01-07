#!/usr/bin/env python
# encoding: utf-8

"""
@description:强制关键词参数

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec02_force_args.py
@time: 2017/1/7 19:36
"""


def recv(maxsize, *, block):
    'receives a message'
    print('receives a message')


def mininum(*values, clip=None):
    m = min(values)
    if clip is not None:
        m = clip if clip > m else m
    return m


def demo():
    # print(recv(1024, True))
    print(recv(1024, block=True))

    print(mininum(1, 5, 2, -5, 10))
    print(mininum(1, 5, 2, -5, 10, clip=0))

    help(recv)


def main():
    demo()


if __name__ == '__main__':
    main()
