#!/usr/bin/env python
# encoding: utf-8

"""
@description: 内存读取

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec10_memory_read.py
@time: 2016/12/26 21:43
"""

import os
import mmap
from xiaocook.util.settings import FILE_PATH

FILE_NAME = FILE_PATH + "data.bin"


def memory_map(filename, access=mmap.ACCESS_WRITE):
    size = os.path.getsize(filename)
    fd = os.open(filename, os.O_RDWR)
    return mmap.mmap(fd, size, access=access)


def file_to_memory():
    size = 10000
    with open(FILE_NAME, 'wb') as f:
        f.seek(size - 1)
        f.write(b'\x01')

    m = memory_map(FILE_NAME)
    print(len(m))
    print(m[0:10])
    m[0:11] = b'Hello World'
    m.close()

    with open(FILE_NAME, 'rb') as f:
        print(f.read(11))

    # 只读操作
    m = memory_map(FILE_NAME, mmap.ACCESS_READ)
    # 只是本地修改，不回写文件
    m = memory_map(FILE_NAME, mmap.ACCESS_COPY)


def memory_view():
    m = memory_map(FILE_NAME)
    v = memoryview(m).cast('I')
    v[0] = 7
    print(m[0:4])
    m[0:4] = b'\x07\x01\x00\x00'
    print(v[0])


def main():
    # file_to_memory()
    memory_view()


if __name__ == '__main__':
    main()
