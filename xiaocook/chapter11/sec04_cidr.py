#!/usr/bin/env python
# encoding: utf-8

"""
@description: 生成ip地址集

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec04_cidr.py
@time: 2017/3/16 18:37
"""

import ipaddress


def ip_demo():
    net = ipaddress.ip_network('123.45.67.64/27')
    print(net)
    for a in net:
        print(a)

    net6 = ipaddress.ip_network('12:3456:78:90ab:cd:ef01:23:30/125')
    for a in net6:
        print(a)

    print(net.num_addresses)
    print(net[5])

    b = ipaddress.ip_address('123.45.67.123')
    print(b in net)

    inet = ipaddress.ip_interface('123.45.67.73/27')
    print(inet.network)
    print(inet.ip)


def ip_demo2():
    a = ipaddress.ip_address('127.0.0.1')
    from socket import socket, AF_INET, SOCK_STREAM
    s = socket(AF_INET, SOCK_STREAM)
    print(s.connect((str(a), 8080)))


def main():
    # ip_demo()
    ip_demo2()


if __name__ == '__main__':
    main()
