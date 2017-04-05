#!/usr/bin/env python
# encoding: utf-8

"""
@description: 装饰器需要保留原始的函数或者类的元信息

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec02_wrap_meta.py
@time: 2017/4/5 20:32
"""
import time
from functools import wraps
from inspect import signature


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


def wrapper_meta():
    print(count_down.__name__)
    print(count_down.__doc__)
    print(count_down.__annotations__)

    # 访问原始函数
    print(count_down.__wrapped__(10000))

    print(signature(count_down))


def main():
    wrapper_meta()


if __name__ == '__main__':
    main()
