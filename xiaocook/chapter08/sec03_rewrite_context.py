#!/usr/bin/env python
# encoding: utf-8

"""
@description: 实现上下文管理器

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec03_rewrite_context.py
@time: 2017/1/8 16:27
"""

from socket import socket, AF_INET, SOCK_STREAM
from functools import partial


class LazyConnection:
    def __init__(self, addr, family=AF_INET, type=SOCK_STREAM):
        self.addr = addr
        self.family = family
        self.type = type
        self.sock = None

    def __enter__(self):
        if self.sock is not None:
            raise RuntimeError('Already connetcted')
        self.sock = socket(self.family, self.type)
        self.sock.connect(self.addr)
        return self.sock

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.sock.close()
        self.sock = None


def ctx_demo():
    conn = LazyConnection('www.python.org', 80)
    with conn as s:
        s.send(b'GET /index.html HTTP/1.1\r\n')
        s.send(b'Host: www.python\r\n')
        s.send(b'\r\n')
        resp = b''.join(iter(partial(s.recv, 8192), b''))
        print(resp.decode())


def main():
    ctx_demo()


if __name__ == '__main__':
    main()
