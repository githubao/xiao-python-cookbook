#!/usr/bin/env python
# encoding: utf-8

"""
@description: 上下文管理器

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec22_contextmanager.py
@time: 2017/4/10 21:02
"""

import time
from contextlib import contextmanager
import random


@contextmanager
def timethis(label):
    start = time.time()

    try:
        yield
    finally:
        end = time.time()
        print('{}: {}'.format(label, end - start))


def demo1():
    with timethis('counting'):
        time.sleep(random.random())


@contextmanager
def list_transaction(orig_list):
    working = list(orig_list)
    yield working
    orig_list[:] = working


def demo2():
    items = [1, 2, 3]
    with list_transaction(items) as working:
        working.append(4)
        working.append(5)

    print(items)


def main():
    demo2()


if __name__ == '__main__':
    main()
