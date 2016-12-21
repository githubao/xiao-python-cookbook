#!/usr/bin/env python
# encoding: utf-8

"""
@description: 给切片命名

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec11_naming_slice.py
@time: 2016/12/7 22:38
"""

record = '....................100 .......513.25.........'


def name_slice():
    cost = int(record[20:23]) * float(record[31:37])
    print(cost)

    SHARES = slice(20, 23)
    PRICE = slice(31, 37)
    cost = int(record[SHARES]) * float(record[PRICE])
    print(cost)


def slice_demo():
    items = [0, 1, 2, 3, 4, 5, 6]
    a = slice(2, 4)
    print(a)

    print(items[2:4])
    print(items[a])

    items[a] = [10, 11]
    print(items)

    del items[a]
    print(items)


def indices_demo():
    a = slice(5, 50, 2)
    print(a.start)
    print(a.stop)
    print(a.step)
    print(a)

    s = 'HelloWorld'
    print(a.indices(len(s)))

    for i in range(*a.indices(len(s))):
        print(s[i])


def main():
    # name_slice()
    slice_demo()
    indices_demo()


if __name__ == '__main__':
    main()
