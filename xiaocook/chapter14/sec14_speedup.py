#!/usr/bin/env python
# encoding: utf-8

"""
@description: 计算程序的运行

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec14_speedup.py
@time: 2017/4/12 13:13
"""

'''
1, 定义函数，局部变量而不是全局变量
2，尽量减少“点号”属性访问
3，使用from math import sqrt 而不是import math
'''

from math import sqrt
import math
import time
from functools import wraps


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
def compute_roots(top):
    result = []
    result_append = result.append

    for n in range(top):
        result_append(sqrt(n))

    return result


@timethis
def compute_roots_slow(top):
    result = []

    for n in range(top):
        result.append(math.sqrt(n))

    return result


class A:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value


def main():
    compute_roots(100000)
    compute_roots_slow(100000)


if __name__ == '__main__':
    main()
