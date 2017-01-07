#!/usr/bin/env python
# encoding: utf-8

"""
@description: 多个关键词参数

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec01_many_args.py
@time: 2017/1/3 22:36
"""

import html


def avg(first, *rest):
    return (first + sum(rest)) / (1 + len(rest))


def args_demo():
    print(avg(1, 2))
    print(avg(1, 2, 3, 4))


def make_element(name, value, **attrs):
    keyvals = [' {}="{}"'.format(k, v) for k, v in attrs.items()]
    attr_str = ''.join(keyvals)
    elements = '<{name}{attrs}>{value}</{name}>'.format(
            name=name,
            attrs=attr_str,
            value=html.escape(value)
    )
    return elements


def main():
    args_demo()
    print(make_element('item', 'xiao', size='large', quantity=6))


if __name__ == '__main__':
    main()
