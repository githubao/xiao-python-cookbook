#!/usr/bin/env python
# encoding: utf-8

"""
@description: lambda 表达式捕获值

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec06_lambda_fetch.py
@time: 2017/1/7 20:06
"""


def fetch_demo():
    x = 10
    a = lambda y: x + y
    print(a(3))

    x = 20
    print(a(3))


def fetch_demo2():
    x = 10
    a = lambda y, x=x: x + y
    print(a(3))

    x = 20
    print(a(3))


def fetch_demo3():
    funcs = [lambda x, n=n: x + n for n in range(5)]
    for f in funcs:
        print(f(1))

def main():
    fetch_demo()
    fetch_demo2()
    fetch_demo3()


if __name__ == '__main__':
    main()
