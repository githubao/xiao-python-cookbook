#!/usr/bin/env python
# encoding: utf-8

"""
@description: socket 传递

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec11_socket_transfer.py
@time: 2017/3/28 22:45
"""

import multiprocessing
from multiprocessing.reduction import recv_handle, send_handle
from multiprocessing.connection import Listener, Client
import socket
import os
import struct


def worker(in_p, out_p):
    out_p.close()
    while True:
        fd = recv_handle(in_p)
        print('CHILD: GOT FD ', fd)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM, fileno=fd) as s:
            while True:
                msg = s.recv(1024)
                if not msg:
                    break
                print('CHILD: RECV {!r}'.format(msg))
                s.send(msg)


def server(address, in_p, out_p, worker_pid):
    in_p.close()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    s.bind(address=address)
    s.listen(1)

    while True:
        client, addr = s.accept()
        print('SERVER: Got connection from ', addr)
        send_handle(out_p, client.fileno(), worker_pid)
        client.close()


def server_run():
    c1, c2 = multiprocessing.Pipe()
    worker_p = multiprocessing.Process(target=worker, args=(c1, c2))
    worker_p.start()

    server_p = multiprocessing.Process(target=server, args=(('', 15000), c1, c2, worker_p.pid))
    server_p.start()

    c1.close()
    c2.close()


# 获取文件套接字的另外一种实现
def send_fd(sock, fd):
    sock.sendmsg([b'x'], [(socket.SOL_SOCKET, socket.SCM_TIGHTS, struct.pack('i', fd))])
    ack = sock.recv(2)
    assert ack == b'OK'


def recv_fd(sock):
    msg, ancdata, flags, addr = sock.recvmsg(1, socket.CMSG_LEN(struct.calcsize('i')))
    cmsg_level, cmsg_type, cmsg_data = ancdata[0]
    assert cmsg_level == socket.SOL_SOCKET and cmsg_type == socket.SCM_RIGHTS
    sock.sendall(b'OK')

    return struct.unpack('i', cmsg_data)[0]


# 使用文件套接字实现上线的逻辑
def server2(work_address, port):
    work_serv = Listener(work_address, authkey=b'peekaboo')
    worker = work_serv.accept()
    worker_pid = worker.recv()

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    s.bind(('', port))
    s.listen(1)

    while True:
        client, addr = s.accept()
        print('SERVER: Got connection from ', addr)

        # send_handle(worker, client.fileno(), worker_pid)
        send_fd(worker, client.fileno())
        client.close()


def server2_run():
    import sys
    if len(sys.argv) != 3:
        print('Usage: server.py server_address port', file=sys.stderr)
        raise SystemError(-1)
    server2(sys.argv[1], int(sys.argv[2]))


def worker_2(server_address):
    serv = Client(server_address, authkey=b'peekaboo')
    serv.send(os.getpid())
    while True:
        # fd = recv_handle(serv)
        fd = recv_fd(serv)
        print('WORKER: GOT FD ', fd)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            while True:
                msg = client.recv(1024)
                if not msg:
                    break
                print('WORKER: RECV {!r}'.format(msg))
                client.send(msg)


def worker2_run():
    import sys
    if len(sys.argv) != 2:
        print('Usage: worker.py server_address', file=sys.stderr)
        raise SystemError(-1)

    worker2_run()


def main():
    server_run()


if __name__ == '__main__':
    main()
