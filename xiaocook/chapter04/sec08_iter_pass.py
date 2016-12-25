#!/usr/bin/env python
# encoding: utf-8

"""
@description: 迭代器上的一些操作

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec08_iter_pass.py
@time: 2016/12/25 17:27
"""

from itertools import dropwhile, islice


def iter_ignore():
    with open(__file__, encoding='utf-8') as f:
        # 不要文件里面的注释行
        # 创建一个迭代器，只要函数predicate(item)为True，就丢弃iterable中的项，如果predicate返回False，就会生成iterable中的项和所有后续项。
        for line in dropwhile(lambda line: line.strip().startswith('#'), f):
            # for line in dropwhile(lambda item: 'def' in item, f):
            print(line, end='')

    # 与上面 只过滤开头的注释不同，这里过滤所有注释
    with open(__file__, encoding='utf-8') as f:
        lines = (line for line in f if not line.strip().startswith('#'))
        for line in lines:
            print(line, end='')

    items = ['a', 'b', 'c', 1, 4, 10, 15]
    for num in islice(items, 3, None):
        print(num)

    for num in dropwhile(lambda x: isinstance(x, str), items):
        print(num)


def main():
    iter_ignore()


if __name__ == '__main__':
    main()
