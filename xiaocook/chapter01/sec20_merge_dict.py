#!/usr/bin/env python
# encoding: utf-8

"""
@description: 合并多个字典

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec20_merge_dict.py
@time: 2016/12/9 20:51
"""
from collections import ChainMap


def merge_dict():
    a = {'x': 1, 'z': 3}
    b = {'y': 2, 'z': 4}
    c = ChainMap(a, b)
    for key, value in c.items():
        print(key, ": ", value)

    # 对chainmap的操作，只会影响第一个变量
    c['z'] = 10
    c['w'] = 40
    print(a)

    del c['x']
    print(a)

    # del c['y']
    # print(a)


def scope_var():
    values = ChainMap()
    values['x'] = 1
    values = values.new_child()
    values['x'] = 2
    values = values.new_child()
    values['x'] = 3
    print(values)

    print(values['x'])
    values = values.parents
    print(values['x'])
    values = values.parents
    print(values['x'])
    print(values)


def upt_and_chain():
    a = {'x': 1, 'z': 3}
    b = {'y': 2, 'z': 4}

    merged = dict(b)
    merged.update(a)
    a['x'] = 10
    print(merged['x'])

    merged2 = ChainMap(a, b)
    merged2['x'] = 10
    print(merged2['x'])


def main():
    # merge_dict()
    # scope_var()
    upt_and_chain()


if __name__ == '__main__':
    main()
