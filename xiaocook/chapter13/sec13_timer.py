#!/usr/bin/env python
# encoding: utf-8

"""
@description: 实现一个计时器

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec13_timer.py
@time: 2017/4/5 19:52
"""

import time
import random


class Timer:
    def __init__(self, func=time.perf_counter):
        self.elapsed = 0.0
        self._func = func
        self._start = None

    def start(self):
        if self._start is not None:
            raise RuntimeError('Already started')
        self._start = self._func()

    def stop(self):
        if self._start is None:
            raise RuntimeError('Not Started')
        end = self._func()

        self.elapsed += end - self._start
        self._start = None

    def reset(self):
        self.elapsed = 0.0

    @property
    def running(self):
        return self._start is not None

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop()


def fun():
    time.sleep(random.random())


def timeit():
    with Timer() as t:
        fun()
    print(t.elapsed)


def main():
    timeit()


if __name__ == '__main__':
    main()
