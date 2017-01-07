#!/usr/bin/env python
# encoding: utf-8

"""
@description: 函数返回多个参数

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec04_multi_return.py
@time: 2017/1/7 19:43
"""


def myfun():
    return 1,2,3

def return_many():
    print(myfun())
    a,_,c = myfun()
    print(a)
    print(c)


def main():
    return_many()


if __name__ == '__main__':
    main()

