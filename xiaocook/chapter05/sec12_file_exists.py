#!/usr/bin/env python
# encoding: utf-8

"""
@description: 测试文件是否存在

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec12_file_exists.py
@time: 2017/1/2 13:23
"""
import os
import time

from xiaocook.settings import FILE_PATH

file_name = FILE_PATH + 'data.bin'


def file_exists():
    print(os.path.exists(file_name))
    print(os.path.isdir(file_name))
    print(os.path.isfile(file_name))
    print(os.path.islink(file_name))
    # 如果是符号连接的话，打印真实路径
    print(os.path.realpath(file_name))

    print(os.path.getsize(file_name))
    # 上次修改时间
    print(time.ctime(os.path.getmtime(file_name)))

def main():
    file_exists()


if __name__ == '__main__':
    main()
