#!/usr/bin/env python
# encoding: utf-8

"""
@description: 字符串对齐

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec13_str_align.py
@time: 2016/12/24 15:15
"""


def align():
    text = 'Hello World'
    print(text.ljust(20))
    print(text.rjust(20))
    print(text.center(20))

    print(text.ljust(20, '='))
    print(text.center(20, '*'))

def align_using_format():
    text = 'Hello World'

    print(format(text,'>20'))
    print(format(text,'<20'))
    print(format(text,'^20'))

    print(format(text,'=>20s'))
    print(format(text,'*^20s'))

    print('{:>10s}{:>10s}'.format('Hello','World'))
    x = 1.2345
    print(format(x,'>10'))
    print(format(x,'^10.2f'))

def main():
    # align()
    align_using_format()


if __name__ == '__main__':
    main()
