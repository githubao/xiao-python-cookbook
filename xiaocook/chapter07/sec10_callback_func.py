#!/usr/bin/env python
# encoding: utf-8

"""
@description: 回调函数

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec10_callback_func.py
@time: 2017/1/8 15:05
"""


def apply_async(func, args, *, callback):
    result = func(*args)

    callback(result)


def print_result(result):
    print('Got: {}'.format(result))


def add(x, y):
    return x + y


class RequestHandler():
    def __init__(self):
        self.sequence = 0

    def handler(self, result):
        self.sequence += 1
        print('[{}] Got: {}'.format(self.sequence, result))


def make_handler():
    sequence = 0

    def handler(result):
        nonlocal sequence
        sequence += 1
        print('[{}] Got: {}'.format(sequence, result))

    return handler


def make_handler2():
    sequence = 0
    while True:
        result = yield
        sequence += 1
        print('[{}] Got: {}'.format(sequence, result))


def callback_demo():
    apply_async(add, (2, 3), callback=print_result)


def callback_demo2():
    r = RequestHandler()

    for i in range(3):
        apply_async(add, (2, 3), callback=r.handler)


def callback_demo3():
    handler = make_handler()

    for i in range(3):
        apply_async(add, (2, 3), callback=handler)

def callback_demo4():
    handler = make_handler2()
    next(handler)

    for i in range(3):
        apply_async(add, (2, 3), callback=handler.send)


def main():
    # callback_demo()
    # callback_demo2()
    # callback_demo3()
    callback_demo4()


if __name__ == '__main__':
    main()
