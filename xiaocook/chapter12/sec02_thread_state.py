#!/usr/bin/env python
# encoding: utf-8

"""
@description: 多个线程之间的信息传递

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec02_thread_state.py
@time: 2017/4/3 16:18
"""

from threading import Thread, Event, Condition, Semaphore
import time


def countdown(n, start_evt):
    print('countdown starting')
    start_evt.set()
    while n > 0:
        print('T-minus: ', n)
        n -= 1
        time.sleep(1)


def run():
    start_evt = Event()
    t = Thread(target=countdown, args=(5, start_evt))
    t.start()

    # 让线程等着，直到某时刻这个变量被调用set()设置为True
    start_evt.wait()

    print('countdown running')


class PeriodTimer:
    def __init__(self, interval):
        self._interval = interval
        self._flag = 0
        self._cv = Condition()

    def start(self):
        t = Thread(target=self.run)
        t.daemon = True

    def run(self):
        while True:
            time.sleep(self._interval)
            with self._cv:
                self._flag ^= 1
                self._cv.notify_all()

    def wait_for_tick(self):
        with self._cv:
            last_flag = self._flag
            while last_flag == self._flag:
                self._cv.wait()


ptimer = PeriodTimer(1)
ptimer.start()


def countdown2(n):
    while n > 0:
        ptimer.wait_for_tick()
        print('T-minus: ', n)
        n -= 1


def countup2(n):
    start = 0
    while start < n:
        ptimer.wait_for_tick()
        print('Counting: ', n)
        start += 1


def run2():
    Thread(target=countdown2, args=(5,)).start()
    Thread(target=countup2, args=(3,)).start()


def worker(n, sema):
    sema.acquire()
    print('working ', n)


def run3():
    sema = Semaphore(0)
    nworkers = 10

    for n in range(nworkers):
        t = Thread(target=worker, args=(n, sema))
        t.start()

    for _ in range(nworkers):
        # time.sleep(0.3)
        # sema.release()
        pass


def main():
    # run()
    # run2()
    run3()


if __name__ == '__main__':
    main()
