#!/usr/bin/env python
# encoding: utf-8

"""
@description: 手动导入模块

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec10_importlib.py
@time: 2017/3/2 21:36
"""

import importlib


def import_demo():
    math = importlib.import_module('math')
    print(math.sin(2))

    # from . import sec01_init
    sec1 = importlib.import_module('.sec01_init', 'xiaocook.chapter10')
    print(sec1)


def main():
    import_demo()


if __name__ == '__main__':
    main()
