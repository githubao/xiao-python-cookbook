#!/usr/bin/env python
# encoding: utf-8

"""
@description:排序值是字典的列表

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec13_sort_dict.py
@time: 2016/12/9 19:27
"""
from operator import itemgetter

rows = [
    {'fname': 'Brain', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'Dvid', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004},
]


def sort_dict():
    rows_by_fname = sorted(rows, key=itemgetter('fname'))
    rows_by_uid = sorted(rows, key=itemgetter('uid'))
    print(rows_by_fname)
    print(rows_by_uid)

    rows_by_lfname = sorted(rows, key=lambda r: (r['lname'], r['fname']))
    # rows_by_lfname = sorted(rows, key=itemgetter('lname', 'fname'))
    print(rows_by_lfname)

    print(min(rows, key=itemgetter('uid')))
    print(max(rows, key=itemgetter('uid')))


def main():
    sort_dict()


if __name__ == '__main__':
    main()
