#!/usr/bin/env python
# encoding: utf-8

"""
@description: 全局锁

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec09_gil.py
@time: 2017/4/4 13:34
"""


def talk_about_gil():
    print('gil 的存在，会导致Python同意时间只能运行一个线程，不能利用多核CPU的优势，不适用于计算密集型的任务')


def main():
    talk_about_gil()


if __name__ == '__main__':
    main()
