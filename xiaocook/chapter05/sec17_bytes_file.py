#!/usr/bin/env python
# encoding: utf-8

"""
@description: 把字节流写到文本文件

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec17_bytes_file.py
@time: 2017/1/2 15:23
"""

import sys


def write():
    # sys.stdout.write(b'Hello\n')
    sys.stdout.buffer.write(b'Hello\n')

def main():
    write()


if __name__ == '__main__':
    main()
