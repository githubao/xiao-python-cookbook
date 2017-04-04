#!/usr/bin/env python
# encoding: utf-8

"""
@description: 定义和实现一个actor任务

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec10_actor_task.py
@time: 2017/4/4 13:50
"""

from queue import Queue
from threading import Thread, Event


class ActorExit(Exception):
    pass


class Actor:
    def __init__(self):
        self._mailbox = Queue()

    def send(self, msg):
        self._mailbox.put(msg)

    def recv(self):
        msg = self._mailbox.get()
        if msg is ActorExit:
            raise ActorExit()
        return msg

    def close(self):
        self.send(ActorExit)

    def start(self):
        self._terminated = Event()
        t = Thread(target=self._bootstrap, daemon=True)
        t.start()

    def _bootstrap(self):
        try:
            self.run()
        except ActorExit:
            pass
        finally:
            self._terminated.set()

    def join(self):
        self._terminated.wait()

    def run(self):
        # while True:
        #     msg = self.recv()
        raise NotImplementedError()


class PrintActor(Actor):
    def run(self):
        while True:
            msg = self.recv()
            print('Got: ', msg)


# 使用生成器实现
def print_actor():
    while True:
        try:
            msg = yield
            print('Got: ', msg)
        except GeneratorExit:
            print('Actor terminating')


def actor_run():
    p = PrintActor()
    p.start()
    p.send('hello')
    p.send('world')

    p.close()
    p.join()


def actor_run2():
    p = print_actor()
    next(p)
    p.send('hello')
    p.send('world')
    p.close()


# 更加高级的actor的实现，发送元组或者运行多个函数
class TaggedActor(Actor):
    def run(self):
        while True:
            tag, *payload = self.recv()
            getattr(self, 'do_' + tag)(*payload)

    def do_A(self, x):
        print('Running A', x)

    def do_B(self, x, y):
        print('Running B', x, y)


def actor_run3():
    a = TaggedActor()
    a.start()
    a.send(('A', 1))
    a.send(('B', 2, 3))

    a.close()
    a.join()


# 获取actor的结果
class Result:
    def __init__(self):
        self._evt = Event()
        self._result = None

    def set_result(self, value):
        self._result = value
        self._evt.set()

    def result(self):
        self._evt.wait()
        return self._result


class WorkerActor(Actor):
    def submit(self, func, *args, **kwargs):
        r = Result()
        self.send((func, args, kwargs, r))
        return r

    def run(self):
        while True:
            func, args, kwargs, r = self.recv()
            r.set_result(func(*args, **kwargs))


def actor_run4():
    w = WorkerActor()
    w.start()
    r = w.submit(pow, 2, 3)
    print(r.result())


def main():
    # actor_run()
    # actor_run2()
    # actor_run3()
    actor_run4()


if __name__ == '__main__':
    main()
