#!/usr/bin/env python
# encoding: utf-8

"""
@description:命名列表

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec18_naming_tuple.py
@time: 2016/12/9 20:27
"""

from collections import namedtuple


def naming_tuple():
    Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
    sub = Subscriber('jonesy@examples.com', '2012-10-19')
    print(sub)
    print(sub.addr)
    print(sub.joined)

    newaddr, newjoined = sub
    print(newaddr)
    print(newjoined)
    print(len(sub))


def stock_example():
    Stock = namedtuple('Stock', ['name', 'shares', 'price'])

    def compute_cost(records):
        total = 0.0
        for rec in records:
            s = Stock(*rec)
            total += s.shares * s.price
        return total


def update_tuple():
    Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])
    stock_prototype = Stock('', 0, 0.0, None, None)

    def dict_to_stock(s):
        return stock_prototype._replace(**s)

    a = {'name': 'ACME', 'shares': 100, 'price': 123.45}
    print(dict_to_stock(a))
    b = {'name': 'ACME', 'shares': 100, 'price': 123.45, 'date': '12/17/2012'}
    print(dict_to_stock(b))


def main():
    # naming_tuple()
    update_tuple()


if __name__ == '__main__':
    main()
