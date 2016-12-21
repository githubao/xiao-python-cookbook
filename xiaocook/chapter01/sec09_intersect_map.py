#!/usr/bin/env python
# encoding: utf-8

"""
@description: 两个map的交集

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec09_intersect_map.py
@time: 2016/12/7 21:01
"""

a = {
    'x': 1,
    'y': 2,
    'z': 3,
}

b = {
    'w': 10,
    'x': 11,
    'y': 2,
}


def inter_operation():
    print(a.keys() & b.keys())
    print(a.keys() - b.keys())
    print(a.items() & b.items())

    c = {key: a[key] for key in a.keys() - {'z', 'w'}}
    print(c)


def main():
    inter_operation()


if __name__ == '__main__':
    main()
