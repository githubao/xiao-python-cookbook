#!/usr/bin/env python
# encoding: utf-8

"""
@description: 线程状态存储

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec06_thread_local.py
@time: 2017/4/4 12:14
"""

from socket import socket, AF_INET, SOCK_STREAM
import threading

from functools import partial


class LazyConnection:
    def __init__(self, address):
        self.address = address
        self.family = AF_INET
        self.type = SOCK_STREAM
        self.local = threading.local()

    def __enter__(self):
        if hasattr(self.local, 'sock'):
            raise RuntimeError('Already connected')

        self.local.sock = socket(self.family, self.type)
        self.local.sock.connect(self.address)
        return self.local.sock

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.local.sock.close()
        del self.local.sock


def test(conn):
    with conn as s:
        s.send(b'GET /index.html HTTP/1.0\r\n')
        s.send(b'HOST: www.python.org\r\n')
        s.send(b'\r\n')
        resp = b''.join(iter(partial(s.recv, 8192), b''))

    print('Got {} bytes'.format(len(resp)))


def run():
    conn = LazyConnection(('www.python.org', 80))

    threads = []

    for i in range(3):
        threads.append(threading.Thread(target=test, args=(conn,)))
        threads[i].start()

    for i in range(3):
        threads[i].join()


def main():
    run()


if __name__ == '__main__':
    main()
