#!/usr/bin/env python
# encoding: utf-8

"""
@description: 创建socket服务器

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec02_socket.py
@time: 2017/3/15 20:58
"""

from socketserver import BaseRequestHandler, TCPServer, StreamRequestHandler, ThreadingTCPServer
from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
from threading import Thread

pool_size = 16


class EchoHandler(BaseRequestHandler):
    def handle(self):
        print('Got connection from: {}'.format(self.client_address))
        while True:

            msg = self.request.recv(8192)
            if not msg:
                break
            self.request.send(msg)


class EchoHandler2(StreamRequestHandler):
    timeout = 5
    rbufsize = -1
    wbufsize = 0
    disable_nagle_algorithm = False

    def handle(self):
        print('Got connection from: {}'.format(self.client_address))
        try:
            for line in self.rfile:
                self.wfile.write(line)
        except socket.timeout:
            print('Time out!')


def server():
    TCPServer.allow_reuse_address = True
    srv = TCPServer(('', 20000), EchoHandler2)
    # srv = ThreadingTCPServer(('', 20000), EchoHandler2)
    srv.serve_forever()


def server_pool():
    srv = TCPServer(('', 20000), EchoHandler2)
    for i in range(pool_size):
        t = Thread(target=srv.serve_forever)
        t.daemon = True
        t.start()

    srv.serve_forever()


def server2():
    srv = TCPServer(('', 20000), EchoHandler, bind_and_activate=False)
    srv.socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, True)
    srv.server_bind()
    srv.server_activate()
    srv.serve_forever()


def client():
    client = socket(AF_INET, SOCK_STREAM)
    client.connect(('localhost', 20000))
    client.send(b'hello')
    print(client.recv(8192))


def main():
    # server_pool()
    server()
    # client()


if __name__ == '__main__':
    main()
