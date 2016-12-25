#!/usr/bin/env python
# encoding: utf-8

"""
@description: 实现一个迭代器

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec02_iter_impl.py
@time: 2016/12/25 14:40
"""


class Node():
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)


def iter_run():
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)

    for child in root:
        print(child)


def main():
    iter_run()


if __name__ == '__main__':
    main()
