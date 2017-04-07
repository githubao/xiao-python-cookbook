#!/usr/bin/env python
# encoding: utf-8

"""
@description: 传参数的装饰器和不传参数的装饰器都可以实现的版本

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec06_args_noargs.py
@time: 2017/4/7 22:58
"""

from functools import wraps, partial
import logging

logging.basicConfig(level=logging.DEBUG)

def logged(func=None, *, level=logging.DEBUG, name=None, message=None):
    if func is None:
        return partial(logged, level=level, name=name, message=message)
    logname = name if name else func.__module__
    log = logging.getLogger(logname)
    logmsg = message if message else func.__name__

    @wraps(func)
    def wrapper(*args, **kwargs):
        log.log(level, logmsg)
        return func(*args, **kwargs)

    return wrapper


@logged
def add(x, y):
    return x + y


@logged(level=logging.CRITICAL, name='example')
def spam():
    s = 'spam'


def main():
    add(2,3)
    spam()


if __name__ == '__main__':
    main()
