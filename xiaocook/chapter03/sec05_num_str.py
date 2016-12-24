#!/usr/bin/env python
# encoding: utf-8

"""
@description: 数字和字符串的互转

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec05_num_str.py
@time: 2016/12/24 23:00
"""

import struct

data = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'


# 密码学 和 网络
def to_str():
    print(len(data))

    print(int.from_bytes(data, 'little'))
    print(int.from_bytes(data, 'big'))

    x = 94522842520747284487117727783387188
    print(x.to_bytes(16, 'big'))
    print(x.to_bytes(16, 'little'))


def using_struct():
    hi, lo = struct.unpack('>QQ', data)
    print((hi << 64) + lo)


# 大端 和 小端
def byte_order():
    x = 0x01020304
    print(x.to_bytes(4, 'big'))
    print(x.to_bytes(4, 'little'))


def big_int():
    x = 523 ** 23
    print(x)

    # print(x.to_bytes(16, 'little'))
    print(x.bit_length())

    nbytes, rem = divmod(x.bit_length(), 8)
    if rem:
        nbytes += 1

    print('len: {}'.format(nbytes))

    print(x.to_bytes(nbytes, 'little'))


def main():
    # to_str()
    # using_struct()
    # byte_order()
    big_int()


if __name__ == '__main__':
    main()
