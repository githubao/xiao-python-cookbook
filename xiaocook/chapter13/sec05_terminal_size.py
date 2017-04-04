#!/usr/bin/env python
# encoding: utf-8

"""
@description: 获取终端的大小

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec05_terminal_size.py
@time: 2017/4/4 18:01
"""

import os


# os.terminal_size(columns=82, lines=15)
def get_size():
    size = os.get_terminal_size()
    print(size)
    print(size.columns)
    print(size.lines)


def main():
    get_size()


if __name__ == '__main__':
    main()
