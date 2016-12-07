#!/usr/bin/env python
# encoding: utf-8

"""
@description:有序字典

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec07_ordered_dict.py
@time: 2016/12/7 20:43
"""

from collections import OrderedDict
import json

def order_dict():
    d = OrderedDict()
    # d = dict()
    d['foo'] = 1
    d['bar'] = 2
    d['spam'] = 3
    d['grok'] = 4
    d['foo'] = 5

    for key in d:
        print(key, d[key])

    j = json.dumps(d)
    print(j)


def main():
    order_dict()


if __name__ == '__main__':
    main()
