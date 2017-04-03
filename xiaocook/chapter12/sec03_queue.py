#!/usr/bin/env python
# encoding: utf-8

"""
@description: 进程间通信的队列

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec03_queue.py
@time: 2017/4/3 16:56
"""

from queue import Queue
import queue
from threading import Thread
import threading
import random
import time
import copy
import heapq

q = Queue()
_sentinel = object()
running = True


def producer(out_q):
    while running:
        data = random.random()
        try:
            # out_q.put(data)
            out_q.put(copy.deepcopy(data), block=False)
        except queue.Full:
            print('queue is Full')

        time.sleep(0.3)

    out_q.put(_sentinel)


def consumer(in_q):
    while True:
        try:
            data = in_q.get(block=False, timeout=3)
        except queue.Empty:
            print('queue is Empty')
        if data is _sentinel:
            break

        name = threading.current_thread().name

        print('{} {}'.format(name, data))

        time.sleep(0.3)


# 自己实现的队列
class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._count = 0
        self._cv = threading.Condition()

    def put(self, item, priority):
        with self._cv:
            heapq.heappush(self._queue, (-priority, self._count, item))
            self._count += 1
            self._cv.notify()

    def get(self):
        with self._cv:
            while len(self._queue) == 0:
                self._cv.wait()
            return heapq.heappop(self._queue)[-1]


def run():
    for i in range(10):
        t1 = Thread(target=consumer, args=(q,))
        t2 = Thread(target=producer, args=(q,))

        t1.start()
        t2.start()

    time.sleep(4)
    global running
    running = False


def main():
    run()


if __name__ == '__main__':
    main()
