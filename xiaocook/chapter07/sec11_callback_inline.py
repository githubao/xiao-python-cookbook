#!/usr/bin/env python
# encoding: utf-8

"""
@description: 回调内联函数

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec11_callback_inline.py
@time: 2017/1/8 15:27
"""

from queue import Queue
from functools import wraps


def apply_async(func, args, *, callback):
    result = func(*args)

    callback(result)


def add(x, y):
    return x + y


class Async():
    def __init__(self, func, args):
        self.func = func
        self.args = args


def inlined_async(func):
    @wraps(func)
    def wrapper(*args):
        f = func(*args)
        result_queue = Queue()
        result_queue.put(None)
        while True:
            result = result_queue.get()

            try:
                a = f.send(result)
                apply_async(a.func, a.args, callback=result_queue.put)
            except StopIteration:
                break

    return wrapper


@inlined_async
def inline_demo():
    r = yield Async(add, (2, 3))
    print(r)
    r = yield Async(add, ("h", "w"))
    print(r)

    for n in range(3):
        r = yield Async(add, (n, n))
        print(r)


def main():
    inline_demo()


if __name__ == '__main__':
    main()
