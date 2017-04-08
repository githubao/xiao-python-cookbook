#!/usr/bin/env python
# encoding: utf-8

"""
@description: 为装饰器函数添加额外的参数

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec11_decorate_args.py
@time: 2017/4/8 11:48
"""

from functools import wraps
import inspect


def optional_debug(func):
    @wraps(func)
    def wrapper(*args, debug=False, **kwargs):
        if debug:
            print('Calling ', func.__name__)
        return func(*args, **kwargs)

    return wrapper


@optional_debug
def spam(a, b):
    print(a, b)


def run1():
    spam(1, 2)
    spam(1, 2, debug=True)


def optional_debug2(func):
    if 'debug' in inspect.signature(func).parameters.values():
        raise TypeError('debug argument already defined')

    @wraps(func)
    def wrapper(*args, debug=False, **kwargs):
        if debug:
            print('Calling ', func.__name__)
        return func(*args, **kwargs)

    sig = inspect.signature(func)
    params = list(sig.parameters.values())
    params.append(inspect.Parameter('debug', inspect.Parameter.KEYWORD_ONLY, default=False))

    wrapper.__signature__ = sig.replace(parameters=params)

    return wrapper


@optional_debug2
def spam2(a, b):
    print(a, b)


def run2():
    spam2(2, 3)
    print(inspect.signature(spam2))


def main():
    # run1()
    run2()


if __name__ == '__main__':
    main()
