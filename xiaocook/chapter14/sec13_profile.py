#!/usr/bin/env python
# encoding: utf-8

"""
@description: 性能测试

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec13_profile.py
@time: 2017/4/11 22:01
"""

import time
from functools import wraps
import random
from contextlib import contextmanager
from timeit import timeit


# 使用time 命令
def timecmd():
    print('time python hello.py')


def profile():
    print('python -m cProfile hello.py')


def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        r = func(*args, **kwargs)
        end = time.perf_counter()
        print('{}.{}: {}'.format(func.__module__, func.__name__, end - start))

        return r

    return wrapper


@timethis
def func():
    time.sleep(random.random())


@contextmanager
def timeblock(label):
    start = time.perf_counter()
    try:
        yield
    finally:
        end = time.perf_counter()
        print('{}: {}'.format(label, end - start))


def func2():
    with timeblock('block time'):
        time.sleep(random.random())


def func3():
    tick = timeit('math.sqrt(2)', 'import math', number=1000000)
    print(tick)


def main():
    # func()
    # func2()
    func3()


if __name__ == '__main__':
    main()
