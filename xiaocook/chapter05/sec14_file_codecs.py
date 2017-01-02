#!/usr/bin/env python
# encoding: utf-8

"""
@description: 文件名的编码和解码

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec14_file_codecs.py
@time: 2017/1/2 13:47
"""

import sys
import os
from xiaocook.util.settings import FILE_PATH


def file_code():
    print(sys.getfilesystemencoding())

    print(os.listdir(FILE_PATH))
    print(os.listdir(FILE_PATH.encode()))


def main():
    file_code()


if __name__ == '__main__':
    main()
