#!/usr/bin/env python
# encoding: utf-8

"""
@description: 删除集合中的重复元素

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec10_dedupe_items.py
@time: 2016/12/7 21:12
"""


def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


def dequpe_no_hash(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


def rm_same():
    a = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
    unique = list(dequpe_no_hash(a, key=lambda d: (d['x'], d['y'])))
    print(unique)

    unique2 = list(dequpe_no_hash(a, key=lambda d: (d['x'])))
    print(unique2)

def main():
    rm_same()


if __name__ == '__main__':
    main()
