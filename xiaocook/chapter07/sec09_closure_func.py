#!/usr/bin/env python
# encoding: utf-8

"""
@description: 闭包函数
返回函数的函数

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec09_closure_func.py
@time: 2017/1/8 14:54
"""

from urllib.request import urlopen


class UrlTemplate():
    def __init__(self, template):
        self.template = template

    def open(self, **kwargs):
        return urlopen(self.template.format_map(kwargs))


def urltemplate(template):
    def opener(**kwargs):
        return urlopen(template.format_map(kwargs))

    return opener


def closure_demo():
    yahoo = UrlTemplate('http://finance.yahoo.com/d/quotes.csv?s={names}&f={fields}')
    for line in yahoo.open(names='IBM,AAPL,FB', fields='sliclv'):
        print(line.decode())


def closure_demo2():
    yahoo = urltemplate('http://finance.yahoo.com/d/quotes.csv?s={names}&f={fields}')
    for line in yahoo(names='IBM,AAPL,FB', fields='sliclv'):
        print(line.decode())

def main():
    # closure_demo()
    closure_demo2()


if __name__ == '__main__':
    main()
