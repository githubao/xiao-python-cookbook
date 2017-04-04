#!/usr/bin/env python
# encoding: utf-8

"""
@description: 线程池

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec07_threadingpools.py
@time: 2017/4/4 12:25
"""

from socket import AF_INET, SOCK_STREAM, socket
from concurrent.futures import ThreadPoolExecutor
from threading import Thread
from queue import Queue
import requests
import threading

# 限制内存栈的大小，默认为8M，一个线程会分配8M的虚拟空间
# 而不是 1024*1024*8
threading.stack_size(65536)


def echo_client(sock, client_addr):
    print('Got connection from ', client_addr)
    while True:
        msg = sock.recv(65536)
        if not msg:
            break
        sock.sendall(msg)
    print('Client closed connection')
    sock.close()


def echo_server(addr):
    pool = ThreadPoolExecutor(128)
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(addr)
    sock.listen(5)
    while True:
        client_sock, client_addr = sock.accept()
        pool.submit(echo_client, client_sock, client_addr)


def echo_client2(q):
    sock, client_addr = q.get()
    print('Got Connection from ', client_addr)
    while True:
        msg = sock.recv(65536)
        if not msg:
            break
        sock.sendall(msg)
    print('Client closed connection')


def echo_server2(addr, nworkers):
    q = Queue()
    for n in range(nworkers):
        t = Thread(target=echo_client2, args=(q,))
        t.daemon = True
        t.start()

    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(address=addr)
    sock.listen(5)
    while True:
        client_sock, client_addr = sock.accept()
        q.put((client_sock, client_addr))


def fetch_url(url):
    return requests.get(url).content.decode()


def server_run():
    echo_server(('', 15000))


def server_run2():
    echo_server2(('', 15000), 128)


def pool_res():
    pool = ThreadPoolExecutor(10)
    a = pool.submit(fetch_url, 'http://www.pypy.org')
    print(a.result()[:128])


def client_run():
    pass


def main():
    pool_res()


if __name__ == '__main__':
    main()
