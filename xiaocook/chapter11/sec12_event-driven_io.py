#!/usr/bin/env python
# encoding: utf-8

"""
@description: 事件驱动的io实现

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec12_event-driven_io.py
@time: 2017/4/3 13:52
"""

import select
import time
import os
import socket
from concurrent.futures import ThreadPoolExecutor


class EventHandler:
    def fileno(self):
        raise NotImplementedError('must implement')

    def wants_to_receive(self):
        return False

    def handle_receive(self):
        pass

    def wants_to_send(self):
        return False

    def handle_send(self):
        pass


def event_loop(handlers):
    while True:
        wants_recv = [h for h in handlers if h.wants_to_receive()]
        wants_send = [h for h in handlers if h.wants_to_send()]

        can_recv, can_send, _ = select.select(wants_recv, wants_send, [])

        for h in wants_recv:
            h.handle_receive()
        for h in can_send:
            h.handle_send()


class UDPServer(EventHandler):
    def __init__(self, address):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(address)

    def fileno(self):
        return self.sock.fileno()

    def wants_to_receive(self):
        return True


class UDPTimeServer(UDPServer):
    def handle_receive(self):
        msg, addr = self.sock.recvfrom(1)
        self.sock.sendto(time.ctime().encode('ascii'), addr)


class UDPEchoServer(UDPServer):
    def handle_receive(self):
        msg, addr = self.sock.recvfrom(8192)
        self.sock.sendto(msg, addr)


class TCPServer(EventHandler):
    def __init__(self, address, client_handler, handler_list):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        self.sock.bind(address)
        self.sock.listen(1)
        self.client_handler = client_handler
        self.handler_list = handler_list

    def fileno(self):
        return self.sock.fileno()

    def wants_to_receive(self):
        return True

    def handle_receive(self):
        client, addr = self.sock.accept()
        self.handler_list.append(self.client_handler(client, self.handler_list))


class TCPClient(EventHandler):
    def __init__(self, sock, handler_list):
        self.sock = sock
        self.handler_list = handler_list
        self.outgoing = bytearray()

    def fileno(self):
        return self.sock.fileno()

    def close(self):
        self.sock.close()
        self.handler_list.remove(self)

    def wants_to_send(self):
        return True if self.outgoing else False

    def handle_send(self):
        nsent = self.sock.send(self.outgoing)
        self.outgoing = self.outgoing[nsent:]


class TCPEchoClient(TCPClient):
    def wants_to_receive(self):
        return True

    def handle_receive(self):
        data = self.sock.recv(8192)
        if not data:
            self.close()
        else:
            self.outgoing.extend(data)


def server_run():
    handlers = [UDPTimeServer(('', 14000)), UDPServer(('', 15000))]
    event_loop(handlers)


# (b'Mon Apr  3 14:14:24 2017', ('127.0.0.1', 14000))
def client_demo():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.sendto(b'', ('localhost', 14000))
    print(s.recvfrom(128))


def server_run2():
    handlers = []
    handlers.append(TCPServer(('', 16000), TCPEchoClient, handlers))
    event_loop(handlers)


def client_demo2():
    # telnet 127.0.0.1 16000
    pass


def client_demo3():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    for x in range(0, 40):
        s.sendto(str(x).encode('ascii'), ('localhost', 16000))
        resp = s.recvfrom(8192)
        print(resp[0])


class ThreadPoolHandler(EventHandler):
    def __init__(self, nworkers):
        if os.name == 'posix':
            self.signal_done_sock, self.done_sock = socket.socketpair()
        else:
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.bind(('127.0.0.1', 0))
            server.listen(1)
            self.signal_done_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.signal_done_sock.connect(server.getsockname())
            self.done_sock, _ = server.accept()
            server.close()

        self.pending = []
        self.pool = ThreadPoolExecutor(nworkers)

    def fileno(self):
        return self.done_sock.fileno()

    def _complete(self, callback, r):
        self.pending.append((callback, r.result()))
        self.signal_done_sock.send(b'x')

    def run(self, func, args=(), kwargs=None, *, callback):
        if kwargs is None:
            kwargs = {}
        r = self.pool.submit(func, *args, **kwargs)
        r.add_done_callback(lambda r: self._complete(callback, r))

    def wants_to_receive(self):
        return True

    def handle_receive(self):
        for callback, result in self.pending:
            callback(result)
            self.done_sock.recv(1)
        self.pending = []


def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


pool = ThreadPoolHandler(16)


class UDPFibServer(UDPServer):
    def handle_receive(self):
        msg, addr = self.sock.recvfrom(128)
        n = int(msg)
        pool.run(fib, (n,), callback=lambda r: self.response(r, addr))

    def response(self, result, addr):
        self.sock.sendto(str(result).encode('ascii'), addr)


def server_run3():
    handlers = [pool, UDPFibServer(('', 16000))]
    event_loop(handlers)


def main():
    # server_run3()
    client_demo3()


if __name__ == '__main__':
    main()
