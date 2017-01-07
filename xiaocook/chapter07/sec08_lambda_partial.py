#!/usr/bin/env python
# encoding: utf-8

"""
@description: 匿名函数

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec08_lambda_partial.py
@time: 2017/1/7 20:01
"""

add = lambda x, y: x + y

names = ['David Beazley', 'Brian Jones', 'Raymond Hettinger', 'Ned Batchelder']


def lambda_demo():
    print(add)
    print(add(2, 3))
    print(add('a', 'b'))

    print(sorted(names, key=lambda name: name.split()[-1].lower()))


def main():
    lambda_demo()


if __name__ == '__main__':
    main()
