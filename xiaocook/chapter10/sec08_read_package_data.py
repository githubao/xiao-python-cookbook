#!/usr/bin/env python
# encoding: utf-8

"""
@description: 使用包相对路径读取文件数据

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec08_read_package_data.py
@time: 2017/3/2 21:18
"""

import pkgutil


def read_data():
    # data = pkgutil.get_data(__package__, '../demo/__init__.py')
    data = pkgutil.get_data('xiaocook.chapter10', 'sec02_all.py')
    print(data.decode())


def main():
    read_data()


if __name__ == '__main__':
    main()
