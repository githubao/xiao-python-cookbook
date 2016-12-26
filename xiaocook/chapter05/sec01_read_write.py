#!/usr/bin/env python
# encoding: utf-8

"""
@description: 读写文本数据

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec01_read_write.py
@time: 2016/12/25 21:33
"""

from xiaocook.util.settings import FILE_PATH
import sys
import traceback


def io():
    with open(FILE_PATH + 'iter_demo_out.txt') as f:
        data = f.read()
        print(data)

    with open(FILE_PATH + 'iter_demo_out.txt') as f:
        for line in f:
            print(line.strip() + '-666')

    with open(FILE_PATH + 'io.txt', 'w', encoding='utf-8') as fw:
        print('aaa', file=fw)
        print('bbb', file=fw)


# ascii latin-1 utf-8 utf-16

def get_file_code():
    print(sys.getdefaultencoding())


# 不会自动处理 \r\n 为\n
def get_end_escase():
    with open(FILE_PATH + 'iter_demo_out.txt', newline='') as f:
        print(f.read)


def handle_err():
    with open(__file__, encoding='ascii') as f:
        try:
            print(f.read())
        except:
            traceback.print_exc()

    with open(__file__, encoding='ascii', errors='replace') as f:
        print(f.read())

    with open(__file__, encoding='ascii', errors='ignore') as f:
        print(f.read())


def main():
    # io()
    # get_file_code()
    # get_end_escase()
    handle_err()


if __name__ == '__main__':
    main()
