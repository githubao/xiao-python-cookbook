#!/usr/bin/env python
# encoding: utf-8

"""
@description: 变量替换 和 格式化字符串

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec15_str_format.py
@time: 2016/12/24 16:19
"""

import sys

s = '{name} has {n} message'


def format_demo():
    name = 'Guido'
    n = 37

    print(s.format(name=name, n=n))
    print(s.format_map(vars()))


# 对象实例
class Info():
    def __init__(self, name, n):
        self.name = name
        self.n = n


def format_instance():
    a = Info('hello', 24)
    print(s.format_map(vars(a)))


# 防止key找不到
class safesub(dict):
    def __missing__(self, key):
        return '{' + key + '}'


def format_with_safe():
    name = 'Guido'

    # print(s.format(name=name))
    # print(s.format_map(vars()))

    print(s.format_map(safesub(vars())))


# 自定义format
def my_sub(text):
    return text.format_map(safesub(sys._getframe(1).f_locals))


def test_my_sub():
    name = 'my'
    n = 12

    print(my_sub('hello {name}'))
    print(my_sub('you have {n} message'))
    print(my_sub('her favorite color is {color}'))


def main():
    # format_demo()
    # format_instance()
    # format_with_safe()
    test_my_sub()


if __name__ == '__main__':
    main()
