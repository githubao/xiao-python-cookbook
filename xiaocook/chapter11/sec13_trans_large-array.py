#!/usr/bin/env python
# encoding: utf-8

"""
@description: 发送和接收大型数组

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec13_trans_large-array.py
@time: 2017/4/3 14:57
"""

import numpy as np
import socket
import time

from socketserver import BaseRequestHandler, TCPServer, StreamRequestHandler, ThreadingTCPServer


def send_from(arr, dest):
    view = memoryview(arr).cast('B')
    while len(view):
        nsent = dest.send(view)
        view = view[nsent:]


def recv_into(arr, source):
    view = memoryview(arr).cast('B')
    while len(view):
        nrecv = source.recv_into(view)
        view = view[nrecv:]


class EchoHandler(BaseRequestHandler):
    def handle(self):
        print('Got connection from: {}'.format(self.client_address))
        while True:

            msg = self.request.recv(8192)
            if not msg:
                break
            self.request.send(msg)


def server_run():
    TCPServer.allow_reuse_address = True
    srv = TCPServer(('', 25000), EchoHandler)
    srv.serve_forever()


def server_run2():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', 25000))
    s.listen(1)
    c, a = s.accept()
    data = s.recv(1024)
    s.sendall(data)

    time.sleep(5 * 60)


def send(c):
    a = np.arange(0.0, 50.0)
    send_from(a, c)
    # c.sendall(a)


def receive(c):
    r = np.zeros(shape=50, dtype=float)
    recv_into(r, c)
    # r = c.recv(1024)
    print(r[0:10])


def send_receive():
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c.connect(('localhost', 25000))

    send(c)
    receive(c)


def main():
    # server_run()
    send_receive()


if __name__ == '__main__':
    main()
