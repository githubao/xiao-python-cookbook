#!/usr/bin/env python
# encoding: utf-8

"""
@description: 包的安装文件

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: setup.py
@time: 2017/3/15 20:17
"""

from distutils.core import setup

setup(
        name='projectname',
        version='1.0',
        author='xiao',
        author_email='mailbaoqiang@gmail.com',
        url='http://www.github.com/githubao',
        # packages=['projectname', 'projectname.util'],
        packages=['demo'],
)


def main():
    print("do sth")


if __name__ == '__main__':
    main()
