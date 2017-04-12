#!/usr/bin/env python
# encoding: utf-8

"""
@description: pdb 调试程序

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec12_debug.py
@time: 2017/4/11 21:55
"""

import traceback
import pdb


def func(n):
    try:
        raise RuntimeError
    except:
        traceback.print_exc()
        traceback.print_stack()

    n = 2
    pdb.set_trace()

    return n + 10


def main():
    func(4)


if __name__ == '__main__':
    main()
