#!/usr/bin/env python
# encoding: utf-8

"""
@description: 打印错误消息并退出

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec02_raise_err.py
@time: 2017/4/4 17:24
"""

import sys


def func1():
    raise SystemExit('it failed!')


def func2():
    sys.stderr.write('it failed!\n')
    raise SystemExit(1)


def main():
    # func1()
    func2()


if __name__ == '__main__':
    main()
