#!/usr/bin/env python
# encoding: utf-8

"""
@description: 例子程序

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: example.py
@time: 2017/4/11 20:30
"""

import csv
from urllib.request import urlopen


def downprices():
    u = urlopen('http://finance.yahoo.com/d/quotes.csv?s=@^DJI&f=sl1')

    lines = (line.decode() for line in u)
    rows = (row for row in csv.reader(lines) if len(row) == 2)
    prices = {name: float(price) for name, price in rows}
    return prices


def func1(x):
    print('func1', x)


def func2(x):
    print('func2', x)


def func3(x):
    print('func3', x)
