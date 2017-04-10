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
@file: sec23_exec.py
@time: 2017/4/10 21:10
"""


def execute():
    a = 2
    loc = locals()
    print(loc)
    exec('b=a+1')
    print(loc)
    locals()
    print(loc)


def good_practice(cmd):
    a = 2
    loc = {'a': a}
    glb = {}
    exec(cmd, glb, loc)
    b = loc['b']

    print(b)


def main():
    # execute()
    good_practice('b=a+3')


if __name__ == '__main__':
    main()
