#!/usr/bin/env python
# encoding: utf-8

"""
@description:装饰器修饰类而不是方法

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec10_decorate_class.py
@time: 2017/4/8 11:30
"""

import time
from functools import wraps
import random
from abc import ABCMeta, abstractmethod


def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        r = func(*args, **kwargs)
        end = time.time()
        print(end - start)
        return r

    return wrapper


class Spam:
    @timethis
    def instance_method(self):
        time.sleep(random.random())

    @classmethod
    @timethis
    def class_method(cls):
        time.sleep(random.random())

    @staticmethod
    @timethis
    def static_method():
        time.sleep(random.random())


def run():
    s = Spam()

    s.instance_method()
    s.class_method()
    s.static_method()


class A(metaclass=ABCMeta):
    @classmethod
    @abstractmethod
    def mothod(cls):
        pass


def main():
    run()


if __name__ == '__main__':
    main()
