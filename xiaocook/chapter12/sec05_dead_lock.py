#!/usr/bin/env python
# encoding: utf-8

"""
@description: 防止死锁的机制

避免死锁的机制：
watchdog:
按照id的顺序获得锁

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec05_dead_lock.py
@time: 2017/4/3 17:38
"""

import threading
from contextlib import contextmanager
import time

_local = threading.local()


@contextmanager
def acquire(*locks_origin):
    locks = sorted(locks_origin, key=lambda x: id(x))

    acquired = getattr(_local, 'acquired', [])
    if acquired and max(id(lock) for lock in acquired) >= id(locks[0]):
        raise RuntimeError('Lock Order Violation')

    acquired.extend(locks)
    _local.acquired = acquired

    try:
        for lock in locks:
            lock.acquire()
        yield
    except Exception as e:
        print(e)
    finally:
        for lock in reversed(locks):
            lock.release()
        del acquired[-len(locks):]


x_lock = threading.Lock()
y_lock = threading.Lock()


def thread1():
    while True:
        with acquire(x_lock, y_lock):
            print('Thread-1')


def thread2():
    while True:
        with acquire(y_lock, x_lock):
            print('Thread-2')


def thread1_dead():
    while True:
        with acquire(x_lock):
            with acquire(y_lock):
                print('Thread-1')


def thread2_dead():
    while True:
        with acquire(y_lock):
            with acquire(x_lock):
                print('Thread-2')


def run():
    # t1 = threading.Thread(target=thread1,daemon=True)
    t1 = threading.Thread(target=thread1_dead, daemon=True)
    t1.start()

    # t2 = threading.Thread(target=thread2,daemon=True)
    t2 = threading.Thread(target=thread2_dead, daemon=True)
    t2.start()

    time.sleep(10)


def philosopher(left, right):
    while True:
        with acquire(left, right):
            print(threading.current_thread(), 'eating')


def run2():
    NSTICKS = 5
    chopstaicks = [threading.Lock() for _ in range(NSTICKS)]

    for n in range(NSTICKS):
        t = threading.Thread(target=philosopher, args=(chopstaicks[n], chopstaicks[(n + 1) % NSTICKS]))
        t.start()


def main():
    # run()
    run2()


if __name__ == '__main__':
    main()
