#!/usr/bin/env python
# encoding: utf-8

"""
@description: 使用生成器实现迭代

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec03_generator_next.py
@time: 2016/12/25 15:13
"""


def frange(start, stop, increment):
    x = start
    while x < stop:
        yield x
        x += increment


def generate():
    for n in frange(0, 4, 0.5):
        print(n)

    print(list(frange(0, 1, 0.3)))


def countdown(n):
    print('starting to count from: ', n)
    while n > 0:
        yield n
        n -= 1
    print('Done')

def generator_next():
    c = countdown(3)
    print(next(c))
    print(next(c))
    print(next(c))
    print(next(c))


def main():
    # generate()
    generator_next()


if __name__ == '__main__':
    main()
