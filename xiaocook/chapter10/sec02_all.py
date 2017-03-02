#!/usr/bin/env python
# encoding: utf-8

"""
@description: 使用all属性控制模块的精确导入

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec02_all.py
@time: 2017/3/2 20:32
"""

from xiaocook.chapter10.sec01_init import *


def demo():
    spam()
    grok()

    # print(blah)

def main():
    demo()


if __name__ == '__main__':
    main()
