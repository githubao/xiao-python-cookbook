#!/usr/bin/env python
# encoding: utf-8

"""
@description: 创建启动停止和销毁线程

由于GIL的原因，多线程只适用于IO密集型的任务，不适用与CPU密集型的任务

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec01_start_stop.py
@time: 2017/4/3 15:59
"""

import time
from threading import Thread
import multiprocessing
import sys
import socket


def countdown(n):
    while n > 0:
        print('T-minus:', n)
        n -= 1
        time.sleep(1)


def run():
    t = Thread(target=countdown, args=(5,))
    # 无法调用join，主线程结束的时候，必然会被终止
    # t = Thread(target=countdown, args=(5,), daemon=True)
    t.start()

    time.sleep(2.5)
    if t.is_alive():
        print('is alive')

    # t.join()

    sys.exit(-1)


def run2():
    p = multiprocessing.Process(target=countdown, args=(5,))
    p.start()


# 自己实现是否什么时候终止线程的操作
class CountdownTask:
    def __init__(self):
        self._running = True

    def terminate(self):
        self._running = False

    def run(self, n):
        while self._running and n > 0:
            print('T-minus:', n)
            n -= 1
            time.sleep(1)


class IOTask:
    def terminate(self):
        self._running = False

    def run(self, sock):
        sock.settimeout(5)

        while self._running:
            try:
                data = sock.recv(8192)
                break
            except socket.socket.timeout:
                continue

        return


def main():
    # run()
    run2()


if __name__ == '__main__':
    main()
