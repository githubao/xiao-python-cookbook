#!/usr/bin/env python
# encoding: utf-8

"""
@description: 协程

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec12_coroutine.py
@time: 2017/4/4 14:35
"""

from collections import deque
from select import select
from socket import socket, AF_INET, SOCK_STREAM
import time


def count_down(n):
    while n > 0:
        print('T-minus ', n)
        yield
        n -= 1
    print('Blast off!')


def count_up(n):
    x = 0
    while x < n:
        print('counting up', x)
        yield
        x += 1
    print('Blast up!')


class TaskScheduler:
    def __init__(self):
        self._task_queue = deque()

    def new_task(self, task):
        self._task_queue.append(task)

    def run(self):
        while self._task_queue:
            task = self._task_queue.popleft()
            try:
                next(task)
                self._task_queue.append(task)
            except StopIteration:
                pass


def coroutine1():
    sched = TaskScheduler()
    sched.new_task(count_down(10))
    sched.new_task(count_down(5))
    sched.new_task(count_up(15))

    sched.run()


class ActorScheduler:
    def __init__(self):
        self._actor = {}
        self._msg_queue = deque()

    def new_actor(self, name, actor):
        self._msg_queue.append((actor, None))
        self._actor[name] = actor

    def send(self, name, msg):
        actor = self._actor.get(name)
        if actor:
            self._msg_queue.append((actor, msg))

    def run(self):
        while self._msg_queue:
            actor, msg = self._msg_queue.popleft()

            try:
                actor.send(msg)
            except StopIteration:
                pass


def printer():
    while True:
        msg = yield
        print('Got: ', msg)


def counter(sched):
    while True:
        n = yield
        if n == 0:
            break
        sched.send('printer', n)
        sched.send('counter', n - 1)


def coroutine_actor():
    sched = ActorScheduler()
    sched.new_actor('printer', printer())
    sched.new_actor('counter', counter(sched))

    sched.send('counter', 100)
    sched.run()


def generator_sample():
    def some_generator():
        data = 'msg'
        result = yield data

    f = some_generator()
    result = None
    while True:
        try:
            data = f.send(result)
            print(data)
        except StopIteration:
            break


class YieldEvent:
    def handle_yield(self, sched, task):
        pass

    def handle_resume(self, sched, task):
        pass


class Scheduler:
    def __init__(self):
        self._numtasks = 0
        self._ready = deque()
        self._read_waiting = {}
        self._write_waiting = {}

    def _iopool(self):
        rset, wset, eset = select(self._read_waiting, self._write_waiting, [])
        for r in rset:
            evt, task = self._read_waiting.pop(r)
            evt.handle_resume(self, task)
        for w in wset:
            evt, task = self._write_waiting.pop(w)
            evt.handle_resume(self, task)

    def new(self, task):
        self._ready.append((task, None))
        self._numtasks += 1

    def add_ready(self, task, msg=None):
        self._ready.append((task, msg))

    def _read_wait(self, fileno, evt, task):
        self._read_waiting[fileno] = (evt, task)

    def _write_wait(self, fileno, evt, task):
        self._write_waiting[fileno] = (evt, task)

    def run(self):
        while self._numtasks:
            if not self._ready:
                self._iopool()
            task, msg = self._ready.popleft()
            try:
                r = task.send(msg)
                if isinstance(r, YieldEvent):
                    r.handle_yield(self, task)
                else:
                    raise RuntimeError('unrecognized yield event')
            except StopIteration:
                self._numtasks -= 1


class ReadSocket(YieldEvent):
    def __init__(self, sock, nbytes):
        self.sock = sock
        self.nbytes = nbytes

    def handle_yield(self, sched, task):
        sched._read_wait(self.sock.fileno(), self, task)

    def handle_resume(self, sched, task):
        data = self.sock.recv(self.nbytes)
        sched.add_ready(task, data)


class WriteSocket(YieldEvent):
    def __init__(self, sock, data):
        self.sock = sock
        self.data = data

    def handle_yield(self, sched, task):
        sched._write_wait(self.sock.fileno(), self, task)

    def handle_resume(self, sched, task):
        nsent = self.sock.send(self.data)
        sched.add_ready(task, nsent)


class AcceptSocket(YieldEvent):
    def __init__(self, sock):
        self.sock = sock

    def handle_yield(self, sched, task):
        sched._read_wait(self.sock.fileno(), self, task)

    def handle_resume(self, sched, task):
        r = self.sock.accept()
        sched.add_ready(task, r)


class Socket:
    def __init__(self, sock):
        self._sock = sock

    def recv(self, maxbytes):
        return ReadSocket(self._sock, maxbytes)

    def send(self, data):
        return WriteSocket(self._sock, data)

    def accept(self):
        return AcceptSocket(self._sock)

    def __getattr__(self, item):
        return getattr(self._sock, item)


def readline(sock):
    chars = []
    while True:
        c = yield sock.recv(1)
        if not c:
            break
        chars.append(c)
        if c == b'\n':
            break
    return b''.join(chars)


class EchoHandler:
    def __init__(self, addr, sched):
        self.sched = sched
        sched.new(self.server_loop(addr))

    def server_loop(self, addr):
        s = Socket(socket(AF_INET, SOCK_STREAM))
        s.bind(addr)
        s.listen(5)
        while True:
            c, a = yield s.accept()
            print('Got Connection from ', a)
            self.sched.new(self.client_handler(Socket(c)))

    def client_handler(self, client):
        while True:
            line = yield from readline(client)
            if not line:
                break
            line = b'Got: ' + line
            while line:
                nsent = yield client.send(line)
                line = line[nsent:]
        client.close()
        print('Client closed')


def yield_from():
    sched = Scheduler()
    EchoHandler(('', 16000), sched)
    sched.run()


def client_test():
    s = socket(AF_INET, SOCK_STREAM)
    s.connect(('localhost', 16000))
    s.send(b'Hello world!\n')
    res = s.recv(1024)
    print(res)


def main():
    # coroutine1()
    # coroutine_actor()
    # generator_sample()
    # yield_from()
    client_test()


if __name__ == '__main__':
    main()
