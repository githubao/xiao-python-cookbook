#!/usr/bin/env python
# encoding: utf-8

"""
@description: 把数据编码成十六进制

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec09_encry_hex.py
@time: 2017/1/2 20:46
"""

import binascii
import base64


def to_hex():
    s = b'i am xiaobao'
    h = binascii.b2a_hex(s)
    h = h.decode('ascii').upper().encode('ascii')

    print(h)
    print(binascii.a2b_hex(h))

    print(base64.b16encode(s))
    print(base64.b16decode(h))

    print(h.decode())


def main():
    to_hex()


if __name__ == '__main__':
    main()
