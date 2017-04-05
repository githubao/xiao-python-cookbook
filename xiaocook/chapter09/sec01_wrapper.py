#!/usr/bin/env python
# encoding: utf-8

"""
@description: 装饰器

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec01_wrapper.py
@time: 2017/4/5 20:27
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
def count_down(n):
    while n > 0:
        n = n - 1


# count_down = timethis(count_down)

def run():
    count_down(10000)


class A:
    @classmethod
    def method(cls):
        pass


class B:
    def method(cls):
        pass

    method = classmethod(method)


def main():
    run()


if __name__ == '__main__':
    main()
