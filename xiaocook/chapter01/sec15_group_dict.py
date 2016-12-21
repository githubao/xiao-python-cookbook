#!/usr/bin/env python
# encoding: utf-8

"""
@description: 通过一个字段对数据分组

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec15_group_dict.py
@time: 2016/12/9 19:51
"""

from operator import itemgetter
from itertools import groupby
from collections import defaultdict

rows = [
    {'address': '5412 N CLARK', 'date': '07/01/2012'},
    {'address': '5148 N CLARK', 'date': '07/04/2012'},
    {'address': '5800 E 58TH', 'date': '07/02/2012'},
    {'address': '2122 N CLARK', 'date': '07/03/2012'},
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
    {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/04/2012'}
]


def group_dict():
    rows.sort(key=itemgetter("date"))
    print(rows)

    for date, items in groupby(rows, key=itemgetter('date')):
        print(date)
        for i in items:
            print(' ', i)


def group_using_list():
    rows_by_date = defaultdict(list)
    for row in rows:
        rows_by_date[row['date']].append(row)

    for key, value in rows_by_date.items():
        print(key)
        for item in value:
            print(' ', item)


def main():
    # group_dict()
    group_using_list()


if __name__ == '__main__':
    main()
