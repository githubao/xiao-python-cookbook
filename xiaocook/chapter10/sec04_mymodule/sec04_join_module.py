#!/usr/bin/env python
# encoding: utf-8

"""
@description: 粘合使用各个模块

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec04_join_module.py
@time: 2017/3/2 20:50
"""

from xiaocook.chapter10 import sec04_mymodule


def demo():
    a = sec04_mymodule.A()
    a.spam()

    b = sec04_mymodule.B()
    b.bar()


def demo2():
    i = 3
    # print(isinstance(i, sec04_mymodule.a.A))


def main():
    # demo()
    demo2()


if __name__ == '__main__':
    main()
