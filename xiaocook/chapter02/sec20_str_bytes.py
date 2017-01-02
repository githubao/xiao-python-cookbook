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
@file: sec20_str_bytes.py
@time: 2016/12/24 18:53
"""

import os
import re

from xiaocook import settings

# FILE_NAME = settings.FILE_PATH + 'test\xf1test.txt'
FILE_NAME = settings.FILE_PATH + 'testatest.txt'


def bytes_str_op():
    data = b'Hello World'
    print(data[0:5])
    print(data.startswith(b'Hello'))
    print(data.split())
    print(data.replace(b'Hello', b'Hello Cruel'))

    data = bytearray(b'Hello World')
    print(data[0:5])
    print(data.startswith(b'Hello'))
    print(data.split())
    print(data.replace(b'Hello', b'Hello Cruel'))

    print("*" * 20)
    data2 = b'FOO:BAR:SPAM'
    print(re.split(b'[:,]', data2))


def bytes_diff_str():
    a = 'Hello World'
    print(a[0])
    print(a[1])

    b = b'Hello World'
    # b = b'\x84\x54'
    print(b[0])
    print(b[1])

    print(b)
    print(b.decode('ascii'))
    # print(b.decode('utf8'))


def bytes_file_op():
    with open(FILE_NAME, 'w', encoding='utf-8') as f:
        f.write('spicy你好')

    print(os.listdir('.'))
    print(os.listdir(b'.'))


def main():
    # bytes_str_op()
    # bytes_diff_str()
    bytes_file_op()


if __name__ == '__main__':
    main()
