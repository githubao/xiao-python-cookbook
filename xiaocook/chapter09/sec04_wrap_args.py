#!/usr/bin/env python
# encoding: utf-8

"""
@description: 带参数的装饰器

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec04_wrap_args.py
@time: 2017/4/5 20:48
"""

from functools import wraps
import logging


def logged(level, name=None, message=None):
    def decorate(func):
        logname = name if name else func.__module__
        logger = logging.getLogger(logname)
        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            logger.log(level, logmsg)
            return func(*args, **kwargs)

        return wrapper

    return decorate


@logged(logging.INFO)
def add(x, y):
    return x + y


# logged(logging.INFO)(add)(x,y)

@logged(logging.CRITICAL)
def spam():
    # print('Spam')
    pass

# logged(logging.INFO)(spam)()

def main():
    # add(3, 4)
    spam()


if __name__ == '__main__':
    main()
