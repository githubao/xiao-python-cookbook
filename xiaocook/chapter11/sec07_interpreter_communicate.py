#!/usr/bin/env python
# encoding: utf-8

"""
@description: 解释器之间通信

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec07_interpreter_communicate.py
@time: 2017/3/22 19:53
"""

from multiprocessing.connection import Listener
from multiprocessing.connection import Client
import traceback


def echo_client(conn):
    try:
        while True:
            msg = conn.recv()
            conn.send(msg)
    except EOFError:
        print('Connection closed')


def echo_server(address, authkey):
    serv = Listener('/mnt/myconn', authkey=b'321')
    # serv = Listener(address=address, authkey=authkey)
    while True:
        try:
            client = serv.accept()

            echo_client(client)
        except Exception:
            traceback.print_exc()


def start_run():
    echo_server(('', 25000), authkey=b'peekaboo')


def client_test():
    c = Client(('/mnt/myconn', 25000), authkey=b'321')
    # c = Client(('localhost', 25000), authkey=b'peekaboo')
    c.send(b'hello')
    print(c.recv().decode())


def main():
    start_run()
    # client_test()


if __name__ == '__main__':
    main()
