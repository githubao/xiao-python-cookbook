#!/usr/bin/env python
# encoding: utf-8

"""
@description: 实现自定义容器

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec14_custom_collections.py
@time: 2017/2/28 21:19
"""

import collections
import bisect


class A(collections.Iterable):
    def __iter__(self):
        pass


class SortedItems(collections.Sequence):
    def __init__(self, initial=None):
        self._items = sorted(initial) if initial is not None else []

    def __getitem__(self, item):
        return self._items[item]

    def __len__(self):
        return len(self._items)

    def add(self, item):
        bisect.insort(self._items, item)


class Items(collections.MutableSequence):
    def __init__(self, initial=None):
        self._items = list(initial) if initial is not None else []

    def __getitem__(self, item):
        print('Getting: {}'.format(item))
        return self._items[item]

    def __setitem__(self, key, value):
        print('Setting: {} to {}'.format(key, value))
        self._items[key] = value

    def __delitem__(self, key):
        print('Deleting: {}'.format(key))
        del self._items[key]

    def insert(self, index, value):
        print('Inserting:', index, value)
        self._items.insert(index, value)

    def __len__(self):
        print('Len')
        return len(self._items)


def demo():
    a = A()


def demo2():
    items = SortedItems([5, 1, 3])
    print(list(items))
    print(items[0], items[-1])
    items.add(2)
    print(list(items))


def demo3():
    items = SortedItems([5, 1, 3])
    print(isinstance(items, collections.Iterable))
    print(isinstance(items, collections.Sequence))
    print(isinstance(items, collections.Container))
    print(isinstance(items, collections.Sized))
    print(isinstance(items, collections.Mapping))


def demo4():
    items = Items()
    items.append(2)


def main():
    # demo()
    # demo2()
    # demo3()
    demo4()


if __name__ == '__main__':
    main()
