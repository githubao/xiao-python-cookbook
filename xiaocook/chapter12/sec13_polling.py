#!/usr/bin/env python
# encoding: utf-8

"""
@description: 轮询的实现

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec13_polling.py
@time: 2017/4/4 16:35
"""

from queue import Queue
import socket
import os
import select
import threading
import time


class PollableQueue(Queue):
    def __init__(self):
        super().__init__()
        if os.name == 'posix':
            self._putsocket, self._getsocket = socket.socketpair()
        else:
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.bind(('127.0.0.1', 0))
            server.listen(1)
            self._putsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self._putsocket.connect(server.getsockname())
            self._getsocket, _ = server.accept()
            server.close()

    def fileno(self):
        return self._getsocket.fileno()

    def put(self, item, **kwargs):
        super().put(item)
        self._putsocket.send(b'x')

    def get(self, **kwargs):
        self._getsocket.recv(1)
        return super().get()


def consumer(queues):
    while True:
        can_read, _, _ = select.select(queues, [], [])
        for r in can_read:
            item = r.get()
            print('Got: ', item)


def server_run():
    q1 = PollableQueue()
    q2 = PollableQueue()
    q3 = PollableQueue()

    t = threading.Thread(target=consumer, args=([q1, q2, q3],))
    # t.daemon = True
    t.start()

    q1.put(1)
    q2.put(10)
    q3.put('hello')
    q2.put('44')


# 一般的，使用非socket的实现，
# 这样的做法不好！
def cosumer2(queues):
    while True:
        for q in queues:
            if not q.empty():
                item = q.get()
                print('Got {}'.format(item))

        time.sleep(0.01)


def event_loop(sockets, queues):
    while True:
        can_read, _, _ = select.select(sockets, [], [], 0.01)
        for r in can_read:
            # handle_read(r)
            print(r.get())
        for q in queues:
            if not q.empty():
                item = q.get()
                print('Got: ', item)


def main():
    server_run()


if __name__ == '__main__':
    main()
