#!/usr/bin/env python
# encoding: utf-8

"""
@description: 简单的客户端认证实现

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec09_simple_auth.py
@time: 2017/3/22 20:21
"""

import hmac
import os
from socket import socket, AF_INET, SOCK_STREAM

secret_key = b'321'


def client_auth(conn, secret_key):
    msg = conn.recv(32)
    hash = hmac.new(secret_key, msg)
    digest = hash.digest()
    conn.send(digest)


def server_auth(conn, secret_key):
    msg = os.urandom(32)
    conn.send(msg)
    hash = hmac.new(secret_key, msg)
    digest = hash.digest()
    response = conn.recv(len(digest))
    return hmac.compare_digest(digest, response)


def echo_handler(client):
    if not server_auth(client, secret_key):
        client.close()
        return
    while True:
        msg = client.recv(8192)
        if not msg:
            break
        client.sendall(msg)


def echo_server(addr):
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(addr)
    s.listen(5)
    while True:
        c, a = s.accept()
        echo_handler(c)


def server_run():
    echo_server(('', 18000))


def client_demo():
    s = socket(AF_INET, SOCK_STREAM)
    s.connect(('localhost', 18000))
    client_auth(s, secret_key)
    s.send(b'hhe\n')
    resp = s.recv(1024)
    print(resp)


def main():
    # server_run()
    client_demo()


if __name__ == '__main__':
    main()
