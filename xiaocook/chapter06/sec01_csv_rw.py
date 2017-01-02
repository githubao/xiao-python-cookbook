#!/usr/bin/env python
# encoding: utf-8

"""
@description: 读写csv文件

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec01_csv_rw.py
@time: 2017/1/2 16:42
"""

import csv
from xiaocook.settings import FILE_PATH
import re

file_name = FILE_PATH + 'airline.csv'
file_name2 = FILE_PATH + 'airline2.csv'
from collections import namedtuple

headers = ['Symbol', 'Price', 'Date', 'Time', 'Change', 'Volume']
rows = [{'Symbol': 'AA', 'Price': 39.48, 'Date': '6/11/2007',
         'Time': '9:36am', 'Change': -0.18, 'Volume': 181800},
        {'Symbol': 'AIG', 'Price': 71.38, 'Date': '6/11/2007',
         'Time': '9:36am', 'Change': -0.15, 'Volume': 195500},
        {'Symbol': 'AXP', 'Price': 62.58, 'Date': '6/11/2007',
         'Time': '9:36am', 'Change': -0.46, 'Volume': 935000}]


def read():
    with open(file_name, 'r') as f:
        f_csv = csv.reader(f)
        headers = next(f_csv)
        Row = namedtuple('Row', headers)

        print(headers)
        for r in f_csv:
            row = Row(*r)
            print(row)

    with open(file_name, 'r') as f:
        f_csv = csv.DictReader(f)
        for row in f_csv:
            print(row)


def write():
    with open(file_name, 'w', newline='') as f:
        f_csv = csv.DictWriter(f, headers)
        f_csv.writeheader()
        f_csv.writerows(rows)


def naming():
    with open(file_name2) as f:
        f_csv = csv.reader(f, delimiter='\t')
        # for row in f_csv:
        #     print(row)

        headers = [re.sub('[^a-zA-Z_]', '_', h) for h in next(f_csv)]
        Row = namedtuple('Row', headers)
        for r in f_csv:
            row = Row(*r)
            print(row)


def conv():
    col_types = [str, float, str, str, float, int]
    with open(file_name) as f:
        f_csv = csv.reader(f)
        headers = next(f_csv)
        for row in f_csv:
            row = tuple(convert(value) for convert, value in zip(col_types, row))
            print(row)

    field_types = [('Price', float),
                   ('Change', float),
                   ('Volume', float)
                   ]

    with open(file_name) as f:
        f_csv = csv.DictReader(f)
        for row in f_csv:
            row.update((key, convertion(row[key])) for key, convertion in field_types)
            print(row)


def main():
    # write()
    # read()
    # naming()
    conv()


if __name__ == '__main__':
    main()
