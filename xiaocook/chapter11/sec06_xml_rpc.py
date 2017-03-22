#!/usr/bin/env python
# encoding: utf-8

"""
@description: 远程调用的实现

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec06_xml_rpc.py
@time: 2017/3/22 19:40
"""

from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.client import ServerProxy


class KeyValueServer():
    _rpc_methods = ['get', 'set', 'delete', 'exists', 'keys']

    def __init__(self, addr):
        self._data = {}
        self._serv = SimpleXMLRPCServer(addr, allow_none=True)

        for name in self._rpc_methods:
            self._serv.register_function(getattr(self, name))

    def get(self, name):
        return self._data[name]

    def set(self, name, value):
        self._data[name] = value

    def delete(self, name):
        del self._data[name]

    def exists(self, name):
        return name in self._data

    def keys(self):
        return list(self._data)

    def serve_forever(self):
        self._serv.serve_forever()


def start_run():
    kvserv = KeyValueServer(('', 15000))
    kvserv.serve_forever()


def call_svr():
    s = ServerProxy('http://127.0.0.1:15000', allow_none=True)
    s.set('foo', 'bar')
    s.set('spam', [1, 2, 3])
    print(s.keys())
    print(s.get('spam'))
    s.delete('spam')
    print(s.exists('spam'))


def main():
    # start_run()
    call_svr()


if __name__ == '__main__':
    main()
