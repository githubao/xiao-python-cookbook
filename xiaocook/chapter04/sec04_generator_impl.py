#!/usr/bin/env python
# encoding: utf-8

"""
@description:

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec04_generator_impl.py
@time: 2016/12/25 15:19
"""


class Node():
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def depth_first(self):
        yield self
        for c in self:
            # !!! yield from 使得内部的返回的迭代器行为，与外界看到的一致
            yield from c.depth_first()

    def depth_first2(self):
        return DepthFirstIterator(self)

    def __iter__(self):
        return iter(self._children)


class DepthFirstIterator():
    def __init__(self, start_node):
        self._node = start_node
        self._children_iter = None
        self._child_iter = None

    def __iter__(self):
        return self

    def __next__(self):
        if self._children_iter is None:
            self._children_iter = iter(self._node)
            return self._node
        elif self._child_iter:
            try:
                next_child = next(self._child_iter)
                return next_child
            except StopIteration:
                self._child_iter = None
                return next(self)
        else:
            self._child_iter = next(self._children_iter).depth_first2()
            return next(self)


def iter_run():
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)

    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(Node(3))
    child1.add_child(Node(4))
    child2.add_child(Node(5))

    for child in root.depth_first2():
        print(child)


def main():
    iter_run()


if __name__ == '__main__':
    main()
