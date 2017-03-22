#!/usr/bin/env python
# encoding: utf-8

"""
@description: rcp 远程调用

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec08_rcp_invoke.py
@time: 2017/3/22 20:01
"""

import pickle
from multiprocessing.connection import Listener
from multiprocessing.connection import Client
from threading import Thread


class RPCHandler:
    def __init__(self):
        self._functions = {}

    def register_function(self, func):
        self._functions[func.__name__] = func

    def handle_connection(self, conn):
        try:
            while True:
                func_name, args, kwargs = pickle.loads(conn.recv())

                try:
                    r = self._functions[func_name](*args, **kwargs)
                    conn.send(pickle.dumps(r))
                except Exception as e:
                    conn.send(pickle.dumps(e))
        except EOFError:
            pass


def rpc_server(handler, address, authkey):
    sock = Listener(address=address, authkey=authkey)
    while True:
        client = sock.accept()
        t = Thread(target=handler.handle_connection, args=(client,))
        t.daemon = True

        t.start()


def start_run():
    def add(x, y):
        return x + y

    def sub(x, y):
        return x - y

    handler = RPCHandler()
    handler.register_function(add)
    handler.register_function(sub)

    rpc_server(handler, ('localhost', 17000), authkey=b'321')


class RPCProxy():
    def __init__(self, conn):
        self._conn = conn

    def __getattr__(self, item):
        def do_rpc(*args, **kwargs):
            self._conn.send(pickle.dumps((item, args, kwargs)))
            result = pickle.loads(self._conn.recv())
            if isinstance(result, Exception):
                raise result
            return result

        return do_rpc


def client_demo():
    client = Client(('localhost', 17000), authkey=b'321')
    proxy = RPCProxy(client)
    print(proxy.add(2, 3))


def main():
    # start_run()
    client_demo()


if __name__ == '__main__':
    main()
