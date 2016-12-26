#!/usr/bin/env python
# encoding: utf-8

"""
@description: 把输出打印到文件

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec02_print_file.py
@time: 2016/12/25 21:46
"""

from xiaocook.util.settings import FILE_PATH


def print_to_file():
    with open(FILE_PATH + 'io.txt', 'a') as f:
        print('append', file=f)


def main():
    print_to_file()


if __name__ == '__main__':
    main()
