#!/usr/bin/env python
# encoding: utf-8

"""
@description: 循环引用的问题的处理

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec23_cycle_ref.py
@time: 2017/3/2 18:38
"""

import weakref


class Node:
    def __init__(self, value):
        self.value = value
        self._parent = None
        self.children = []

    def __repr__(self):
        return 'Node({!r:})'.format(self.value)

    def __str__(self):
        return self.__repr__()

    @property
    def parent(self):
        return None if self._parent is None else self._parent()

    @parent.setter
    def parent(self, node):
        self._parent = weakref.ref(node)

    def add_child(self, child):
        self.children.append(child)
        child.parent = self


def weakref_demo():
    root = Node('parent')
    c1 = Node('child')
    root.add_child(c1)

    print(c1.parent)
    del root
    print(c1.parent)


def main():
    weakref_demo()


if __name__ == '__main__':
    main()
