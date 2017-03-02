#!/usr/bin/env python
# encoding: utf-8

"""
@description:

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec01_init.py
@time: 2017/3/2 20:10
"""

__all__ = ['spam', 'grok']


def spam():
    pass


def grok():
    print('grok')


blah = 42


def main():
    print("using __init__.py for a package waiting for importing")


if __name__ == '__main__':
    main()
