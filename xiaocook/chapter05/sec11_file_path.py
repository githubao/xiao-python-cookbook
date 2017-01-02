#!/usr/bin/env python
# encoding: utf-8

"""
@description: 文件路径操作
os: 操作系统相关的模块
sys: Python语言相关的模块

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec11_file_path.py
@time: 2017/1/2 13:08
"""

import os
from xiaocook.util.settings import FILE_PATH

file_name = FILE_PATH + 'data.bin'


def path_demo():
    # 文件名
    print(os.path.basename(file_name))
    # python 绝对路径文件表示，文件规范化的路径表示形式
    print(os.path.abspath(file_name))
    # 路径名
    print(os.path.dirname(file_name))
    # 路径连接
    print(os.path.join(os.path.dirname(file_name), os.path.basename(file_name)))
    # 展开路径名
    print(os.path.expanduser(file_name))
    # 文件名和扩展名
    print(os.path.splitext(file_name))


def main():
    path_demo()


if __name__ == '__main__':
    main()
