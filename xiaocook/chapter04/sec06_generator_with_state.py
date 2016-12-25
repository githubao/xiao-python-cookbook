#!/usr/bin/env python
# encoding: utf-8

"""
@description: 带有外部状态的生成器

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec06_generator_with_state.py
@time: 2016/12/25 17:17
"""

from collections import deque


class linehistory():
    def __init__(self, lines, histlen=3):
        self.lines = lines
        self.history = deque(maxlen=histlen)

    def __iter__(self):
        for lineno, line in enumerate(self.lines, 1):
            self.history.append((lineno, line))
            yield line

    def clear(self):
        self.history.clear()


def generator_with_history():
    with open(__file__, encoding='utf-8') as f:
        lines = linehistory(f)
        for line in lines:
            if 'this is i' in line:
                for lineno, hline in lines.history:
                    print('{}: {}'.format(lineno, hline), end='')


def call_class_generator():
    f = open(__file__, encoding='utf-8')
    lines = linehistory(f)

    it = iter(lines)
    print(next(it), end='')
    print(next(it), end='')


def main():
    # generator_with_history()
    call_class_generator()


if __name__ == '__main__':
    main()
