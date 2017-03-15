#!/usr/bin/env python
# encoding: utf-8

"""
@description: 安装属于自己的包

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec13_private_pkg.py
@time: 2017/3/15 20:06
"""


def my_pkg():
    print('˜/.local/lib/python3.3/site-packages')
    print('pip install --user pkg')
    print('python setup.py install --user')


def main():
    my_pkg()


if __name__ == '__main__':
    main()
