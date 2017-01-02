#!/usr/bin/env python
# encoding: utf-8

"""
@description: base64的编解码

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec09_encry_base64.py
@time: 2017/1/2 20:52
"""

import base64


def de_en():
    s = b'i am xiaobao'
    h = base64.b64encode(s)

    print(base64.b64encode(s))
    print(base64.b64decode(h))


def main():
    de_en()


if __name__ == '__main__':
    main()
