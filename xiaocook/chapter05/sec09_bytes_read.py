#!/usr/bin/env python
# encoding: utf-8

"""
@description: 读取字节到数据结构

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec09_bytes_read.py
@time: 2016/12/26 21:28
"""

import os.path
from xiaocook.util.settings import FILE_PATH


def read_to_buffer(filename):
    buf = bytearray(os.path.getsize(filename))
    with open(filename, 'rb') as f:
        f.readinto(buf)
    return buf


def read_to_memory():
    with open(FILE_PATH + 'sample.bin', 'wb') as f:
        f.write(b'Hello World')

    buf = read_to_buffer(FILE_PATH + 'sample.bin')
    print(buf)

    buf[0:5] = b'weibo'

    with open(FILE_PATH + 'sample.bin', 'wb') as f:
        f.write(buf)


def main():
    read_to_memory()


if __name__ == '__main__':
    main()
