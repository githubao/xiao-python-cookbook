#!/usr/bin/env python
# encoding: utf-8

"""
@description: 不使用init

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec05_no_init.py
@time: 2017/3/2 21:00
"""


def main():
    print("如果说两个源代码根目录下都有spam.py的文件，那么不使用__init__.py文件，"
          "可以保证使用文件夹名作为特殊的命名空间，从而可以使得两个spam文件都可以被使用而且不被混淆")


if __name__ == '__main__':
    main()
