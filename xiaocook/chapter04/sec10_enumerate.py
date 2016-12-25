#!/usr/bin/env python
# encoding: utf-8

"""
@description: 索引迭代

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec10_enumerate.py
@time: 2016/12/25 17:58
"""
from collections import defaultdict


def enum_iter():
    my_list = ['a', 'b', 'c']
    for idx, val in enumerate(my_list):
        print(idx, val)

    print('*' * 20)
    for idx, val in enumerate(my_list, 1):
        print(idx, val)

    parse_data(__file__)


def parse_data(filename):
    with open(filename, 'rt', encoding='utf-8') as f:
        for lineno, line in enumerate(f, 1):
            filelds = line.split()
            try:
                int(filelds)
            except Exception as e:
                print('Line {}: Parse error: {}'.format(lineno, e))
                break


def enum_file():
    word_summary = defaultdict(list)

    with open(__file__, 'rt', encoding='utf-8') as f:
        lines = f.readlines()

    for idx, line in enumerate(lines, 1):
        words = [w.strip().lower() for w in line.split()]

        for word in words:
            word_summary[word].append(idx)

    for word, linenos in word_summary.items():
        print('word: {{{}}}, linenos: {{{}}}'.format(word, linenos))


def enum_tuple():
    data = [(1, 2), (3, 4), (5, 6), (7, 8)]

    for n, (x, y) in enumerate(data):
        print(n, x, y)


def main():
    # enum_iter()
    # enum_file()
    enum_tuple()


if __name__ == '__main__':
    main()
