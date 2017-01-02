#!/usr/bin/env python
# encoding: utf-8

"""
@description: 写字节数据

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec04_write_bytes.py
@time: 2016/12/25 22:11
"""

from xiaocook.settings import FILE_PATH


def bytes_op():
    with open(FILE_PATH + 'file.bin', 'wb') as f:
        f.write('小包'.encode('utf-8'))

    with open(FILE_PATH + 'file.bin', 'rb') as f:
        print(f.read().decode('utf-8'))


def sep_str_bytes():
    hello = 'Hello'
    for s in hello:
        print(s)

    hello = b'Hello'
    for c in hello:
        print(c)


def main():
    # bytes_op()
    sep_str_bytes()


if __name__ == '__main__':
    main()
