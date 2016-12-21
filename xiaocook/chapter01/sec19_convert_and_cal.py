#!/usr/bin/env python
# encoding: utf-8

"""
@description: 转化和计算

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec19_convert_and_cal.py
@time: 2016/12/9 20:43
"""

import os

nums = [1, 2, 3, 4, 5]


def convert_and_cal():
    print(sum(x * x for x in nums))

    files = os.listdir('.')
    if any(name.endswith('.py') for name in files):
        print('There be python!')
    else:
        print('Sorry, no python.')

    s = ('ACME', 50, 123.45)
    print(','.join(str(x) for x in s))

    portfolio = [
        {'name': 'GOOG', 'shares': 50},
        {'name': 'YHOO', 'shares': 75},
        {'name': 'AOL', 'shares': 20},
        {'name': 'SCOX', 'shares': 65}
    ]
    # min_shares = min(s['shares'] for s in portfolio)
    min_shares = min(portfolio, key=lambda s: s['shares'])
    print(min_shares)


def main():
    convert_and_cal()


if __name__ == '__main__':
    main()
