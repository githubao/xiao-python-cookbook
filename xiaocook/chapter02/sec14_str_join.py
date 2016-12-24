#!/usr/bin/env python
# encoding: utf-8

"""
@description: 字符串拼接

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec14_str_join.py
@time: 2016/12/24 15:29
"""

from xiaocook.util.settings import FILE_PATH

FILE_NAME = FILE_PATH + 'io.txt'


def join_demo():
    parts = ['Is', 'Chicago', 'not', 'Chicago']
    print(' '.join(parts))
    print(','.join(parts))
    print(''.join(parts))

    a = 'Is Chicago'
    b = 'not Chicago?'
    print(a + ' ' + b)
    print('{} {}'.format(a, b))

    c = 'Hello''World'
    print(c)


def no_using_plus():
    data = ['ACME', 50, 91.1]
    print(','.join(str(s) for s in data))

    a, b, c = data
    print(a, b, c, sep=':')


def str_join_in_io():
    chunk1 = 'some data\n'
    chunk2 = 'other data\n'

    f = open(FILE_NAME, 'w', encoding='utf-8')

    size = len(chunk1)
    if size < 1024 * 1024:
        f.write(chunk1 + chunk2)
    else:
        f.write(chunk1)
        f.write(chunk2)

    f.close()


def combine(source, maxsize):
    parts = []
    size = 0
    for part in source:
        parts.append(part)
        size += len(part)
        if size > maxsize:
            yield ''.join(parts)
            parts = []
            size = 0
        yield ''.join(parts)


def use_generator_for_many_str():
    print(''.join(strs()))

    with open(FILE_NAME, 'w', encoding='utf-8') as f:
        for part in strs():
            f.write(part)

    # 分片读文件
    with open(FILE_NAME, 'w', encoding='utf-8') as f:
        for part in combine(strs, 32768):
            f.write(part)


def strs():
    yield 'Is'
    yield 'Chicago'
    yield 'not'
    yield 'Chicago?'


def main():
    # join_demo()
    # no_using_plus()
    str_join_in_io()


if __name__ == '__main__':
    main()
