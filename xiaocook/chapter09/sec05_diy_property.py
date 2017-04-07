#!/usr/bin/env python
# encoding: utf-8

"""
@description: 自定义属性

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec05_diy_property.py
@time: 2017/4/7 22:44
"""

from functools import wraps, partial
import logging

logging.basicConfig(level=logging.DEBUG)


def attach_wrapper(obj, func=None):
    if func is None:
        return partial(attach_wrapper, obj)
    setattr(obj, func.__name__, func)
    return func


def logged(level, name=None, message=None):
    def decorate(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            return func(*args, **kwargs)

        @attach_wrapper(wrapper)
        def set_level(newlevel):
            nonlocal level
            level = newlevel

        @attach_wrapper(wrapper)
        def set_message(newmsg):
            nonlocal logmsg
            logmsg = newmsg

        # @attach_wrapper(wrapper)
        # def get_level():
        #     return level

        wrapper.get_level = lambda: level

        return wrapper

    return decorate


@logged(logging.DEBUG)
def add(x, y):
    return x + y


@logged(logging.CRITICAL, 'example')
def spam():
    s = 'i am spam func'


def main():
    add(3, 4)
    spam()

    add.set_message('add called')
    add(3, 4)

    add.set_level(logging.WARNING)
    add(3, 4)

    print(add.get_level())


if __name__ == '__main__':
    main()
