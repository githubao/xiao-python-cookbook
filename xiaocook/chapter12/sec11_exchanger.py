#!/usr/bin/env python
# encoding: utf-8

"""
@description: 订阅和发布的消息交换机

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec11_exchanger.py
@time: 2017/4/4 14:14
"""

from collections import defaultdict
from contextlib import contextmanager


class Exchange:
    def __init__(self):
        self._subscribers = set()

    def attach(self, task):
        self._subscribers.add(task)

    def detach(self, task):
        self._subscribers.remove(task)

    def send(self, msg):
        for subscriber in self._subscribers:
            subscriber.send(msg)

    @contextmanager
    def subscribe(self, *tasks):
        for task in tasks:
            self.attach(task)

        try:
            yield
        finally:
            for task in tasks:
                self.detach(task)


_exchanges = defaultdict(Exchange)


def get_exchange(name):
    return _exchanges[name]


class Task:
    def send(self, msg):
        print('Got msg: ', msg)


def exchange_run():
    task1 = Task()
    task2 = Task()

    exc = get_exchange('example')
    exc.attach(task1)
    exc.attach(task2)

    exc.send('msg1')
    exc.send('msg2')

    exc.detach(task1)
    exc.detach(task2)


# 在执行任务之前，打印消息
class DisplayMessages:
    def __init__(self):
        self.count = 0

    def send(self, msg):
        self.count += 1
        print('msg[{}]: {!r}'.format(self.count, msg))

        # exec()


def log_data():
    exc = get_exchange('log_exchanger')
    d = DisplayMessages()
    exc.attach(d)

    d.send('run task')

    exc.detach(d)


# 用上下文管理器实现
def exchange_run2():
    task1 = Task()
    task2 = Task()
    exc = get_exchange('examples with context manager')
    with exc.subscribe(task1, task2):
        exc.send('msg1')
        exc.send('msg2')


def main():
    # exchange_run()
    exchange_run2()
    # log_data()


if __name__ == '__main__':
    main()
