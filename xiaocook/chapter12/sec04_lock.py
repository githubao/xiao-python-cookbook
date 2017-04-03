#!/usr/bin/env python
# encoding: utf-8

"""
@description: 锁机制

没有锁的话，很有可能，调用的时候值是4，increase+1之后，值变成了6或者4，而不是期望的5

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec04_lock.py
@time: 2017/4/3 17:25
"""

import threading
import requests


class SharedCounter:
    def __init__(self, initial_value=0):
        self._value = initial_value
        self._value_lock = threading.Lock()

    def incr(self, delta=1):
        with self._value_lock:
            self._value += delta

    def decr(self, delta=1):
        with self._value_lock:
            self._value -= delta


class SharedCounter2:
    # 类级别的锁，对象之间的互斥，而不是调用方法的内部的一小块代码
    _lock = threading.RLock()

    def __init__(self, initial_value=0):
        self._value = initial_value

    def incr(self, delta=1):
        with SharedCounter2._lock:
            self._value += delta

    def decr(self, delta=1):
        with SharedCounter2._lock:
            self._value -= delta


# 并发信号量锁，限制并发个数
class UrlFetcher:
    _fetch_url_sema = threading.Semaphore()

    def fetch_url(self, url):
        with self._fetch_url_sema:
            return requests.get(url)


def main():
    pass


if __name__ == '__main__':
    main()
