#!/usr/bin/env python
# encoding: utf-8

"""
@description: 反向迭代

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec05_iter_reverse.py
@time: 2016/12/25 15:47
"""


def reverse():
    a = [1, 2, 3, 4]
    for x in reversed(a):
        print(x)

    f = open(__file__, encoding='utf-8')
    for line in reversed(list(f)):
        print(line, end='')


class Countdown():
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1

    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1


def my_reverse():
    for rr in Countdown(5):
        print(rr)

    print('*' * 20)

    for rr in reversed(Countdown(5)):
        print(rr)


def main():
    # reverse()
    my_reverse()


if __name__ == '__main__':
    main()
