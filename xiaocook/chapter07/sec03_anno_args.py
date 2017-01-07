#!/usr/bin/env python
# encoding: utf-8

"""
@description: 函数注解参数

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec03_anno_args.py
@time: 2017/1/7 19:41
"""


def add(x: int, y: int) -> int:
    return x + y

def add_demo():
    print(add(3, 5))
    print(add.__annotations__)

def main():
    add_demo()

if __name__ == '__main__':
    main()
