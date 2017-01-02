#!/usr/bin/env python
# encoding: utf-8

"""
@description: 操作文件描述符

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec18_op_fd.py
@time: 2017/1/2 15:25
"""

from xiaocook.settings import FILE_PATH

file_name = FILE_PATH + 'io.txt'

import os
from socket import socket, AF_INET, SOCK_STREAM
import sys


def description():
    fd = os.open(file_name, os.O_WRONLY | os.O_CREAT)
    f = open(fd, 'wt', closefd=False)
    f.write('hello\n')
    f.close()


def echo_client(client_sock, addr):
    print('Got connection from ', addr)

    client_in = open(client_sock.fileno(), 'r', encoding='latin-1', closefd=False)
    client_out = open(client_sock.fileno(), 'w', encoding='latin-1', closefd=False)

    for line in client_in:
        client_out.write('repo: {}'.format(line))
        client_out.flush()

    client_sock.close()


def echo_server(addr):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(addr)
    sock.listen(1)
    while True:
        client, add = sock.accept()
        echo_client(client, addr)


def socket_io():
    pass


def cmd_io():
    bstdout = open(sys.stdout.fileno(), 'wb', closefd=False)
    bstdout.write(b'hhh')
    bstdout.flush()


def main():
    # description()
    cmd_io()


if __name__ == '__main__':
    main()
