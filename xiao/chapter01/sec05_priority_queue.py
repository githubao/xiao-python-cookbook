#!/usr/bin/env python
# encoding: utf-8

"""
@description: heapq 实现的优先级队列

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec05_priority_queue.py
@time: 2016/12/7 19:59
"""

import heapq

class PriorityQueue:
    """
    (-priority, self._index, item) 元素从头到尾的可比较
    """
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)


def priority():
    q = PriorityQueue()
    q.push(Item('foo'), 1)
    q.push(Item('bar'), 5)
    q.push(Item('spam'), 4)
    q.push(Item('grok'), 1)

    for i in range(4):
        print(q.pop())


def test():
    print("{0!r:^20}".format("Hello"))
    print("{0!s:>20}".format("Hello"))

def main():
    # priority()
    test()


if __name__ == '__main__':
    main()
