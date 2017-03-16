#!/usr/bin/env python
# encoding: utf-8

"""
@description: udp

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec03_udp.py
@time: 2017/3/16 17:41
"""

from socketserver import BaseRequestHandler, UDPServer, ThreadingUDPServer
from socket import AF_INET, SOCK_DGRAM
import time
import socket


class TimeHandler(BaseRequestHandler):
    def handle(self):
        print('Got connection from: ', self.client_address)
        msg, sock = self.request
        resp = time.ctime()
        sock.sendto(resp.encode('ascii'), self.client_address)


def server():
    # serv = UDPServer(('', 20000), TimeHandler)
    serv = ThreadingUDPServer(('', 20000), TimeHandler)
    serv.serve_forever()


def client():
    s = socket.socket(AF_INET, SOCK_DGRAM)
    s.sendto(b'23', ('localhost', 20000))
    s.recvfrom(8192)


def time_server(address):
    sock = socket.socket(AF_INET, SOCK_DGRAM)
    sock.bind(address)
    while True:
        msg, addr = sock.recvfrom(8192)
        print('Got message from: ', addr)
        resp = time.ctime()
        sock.sendto(resp.encode('ascii'), addr)


def main():
    # server()
    client()


if __name__ == '__main__':
    main()
