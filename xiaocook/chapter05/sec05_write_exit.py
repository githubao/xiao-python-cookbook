#!/usr/bin/env python
# encoding: utf-8

"""
@description: 写 已经存在的文件

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec05_write_exit.py
@time: 2016/12/25 22:22
"""

from xiaocook.util.settings import FILE_PATH
import os


def write_exits():
    # use 'w' to override
    # with open(FILE_PATH + 'io.txt', 'w') as fw:
    #     fw.write('new\n')

    # file exits err
    # with open(FILE_PATH + 'io.txt', 'x') as fw:
    #     fw.write('new\n')

    filename = FILE_PATH + 'io.txt'
    if not os.path.exists(filename):
        with open(FILE_PATH + 'io.txt', 'x') as fw:
            fw.write('new\n')
    else:
        print('{} already exists!'.format(filename))


def main():
    write_exits()


if __name__ == '__main__':
    main()
