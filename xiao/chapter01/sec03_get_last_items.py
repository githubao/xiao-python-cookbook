#!/usr/bin/env python
# encoding: utf-8

"""
@description: 获取结尾的N个元素

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec03_get_last_items.py
@time: 2016/12/7 12:26
"""

from collections import deque


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for li in lines:
        if pattern in li:
            yield li, previous_lines
        previous_lines.append(li)


def search_lines():
    with open('../files/somefile.txt', 'r', encoding='utf-8') as f:
        for line, prevlines in search(f, 'python', 5):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-' * 20)


def deque_demo():
    q = deque(maxlen=3)
    q.append(1)
    q.append(2)
    q.append(3)
    print(q)

    q.append(4)
    print(q)

    q.append(5)
    print(q)

    q = deque()
    q.append(1)
    q.append(2)
    q.append(3)
    print(q)

    q.appendleft(4)
    print(q)

    print(q.pop())
    print(q)
    print(q.popleft())
    print(q)


def main():
    # search_lines()
    deque_demo()

if __name__ == '__main__':
    main()
