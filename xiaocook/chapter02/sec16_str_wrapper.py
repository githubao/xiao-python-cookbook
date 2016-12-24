#!/usr/bin/env python
# encoding: utf-8

"""
@description: 控制字符串长度

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec16_str_wrapper.py
@time: 2016/12/24 16:38
"""

import textwrap
import os

s = "Look into my eyes, look into my eyes, the eyes, the eyes, " \
    "the eyes, not around the eyes, don't look around the eyes, " \
    "look into my eyes, you're under."


def wrap():
    size = os.get_terminal_size().columns

    print('size: {}'.format(size))

    # size += 20

    print(textwrap.fill(s, size))
    print(textwrap.fill(s, size, initial_indent='  '))
    print(textwrap.fill(s, size, subsequent_indent='  '))


def main():
    wrap()


if __name__ == '__main__':
    main()
