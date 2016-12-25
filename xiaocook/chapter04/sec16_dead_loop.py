#!/usr/bin/env python
# encoding: utf-8

"""
@description: 迭代器处理死循环

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec16_dead_loop.py
@time: 2016/12/25 21:26
"""

import sys

CHUNKSIZE = 8192


def reader(s):
    while True:
        data = s.recv(CHUNKSIZE)
        if data == b'':
            break
        process_data(data)


def reader_iter(s):
    for chunk in iter(lambda: s.recv(CHUNKSIZE), b''):
        process_data(chunk)


def process_data(data):
    print(data)


def iter_loop():
    f = open(__file__, encoding='utf-8')
    for chunk in iter(lambda: f.read(10), ''):
        n = sys.stdout.write(chunk+'\n')
        print(n)
    f.close()


def main():
    iter_loop()


if __name__ == '__main__':
    main()
