#!/usr/bin/env python
# encoding: utf-8

"""
@description: 字符串修剪

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec11_str_trip.py
@time: 2016/12/24 14:52
"""
import re


def trim_str():
    s = ' hello world \n'
    print(s.strip())
    print(s.lstrip())
    print(s.rstrip())

    t = '---hello==='
    print(t.strip('-'))
    print(t.strip('-='))


def complex_trim():
    s = ' hello world \n'
    print(s.replace(' ', ''))
    print(re.sub('\s+', '', s))


def multi_trim(filename):
    with open(filename, encoding='utf-8') as f:
        lines = (line.strip() for line in f)
        for line in lines:
            print(line, end='*\n*')


def main():
    # trim_str()
    # complex_trim()
    multi_trim(__file__)


if __name__ == '__main__':
    main()
