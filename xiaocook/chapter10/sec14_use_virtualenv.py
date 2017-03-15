#!/usr/bin/env python
# encoding: utf-8

"""
@description: 创建和使用自己的python环境

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec14_use_virtualenv.py
@time: 2017/3/15 20:08
"""

import sys


def my_pyenv():
    print('pyenv Spam')
    # 包含使用系统的site-packages
    print('pyenv --system-site-packages Spam')
    print(sys.path)


def main():
    my_pyenv()


if __name__ == '__main__':
    main()
