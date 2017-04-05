#!/usr/bin/env python
# encoding: utf-8

"""
@description: 解包装

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec03_unwrapper.py
@time: 2017/4/5 20:42
"""

import time
from functools import wraps


def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end - start)
        return result

    return wrapper


@timethis
def count_down(n: int):
    '''
    count down nums
    '''
    while n > 0:
        n = n - 1


def unwrapper():
    origin_func = count_down.__wrapped__
    print(origin_func)


# 只会解最外层的wrap

def decorator1(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('decorator 1')
        return func(*args, **kwargs)

    return wrapper


def decorator2(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('decorator 2')
        return func(*args, **kwargs)

    return wrapper


@decorator1
@decorator2
def add(x, y):
    return x + y


def unwrapper2():
    add(3, 4)
    print('-----sep-----')
    print(add.__wrapped__(4, 5))


def main():
    # unwrapper()
    unwrapper2()


if __name__ == '__main__':
    main()
