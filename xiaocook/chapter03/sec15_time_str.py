#!/usr/bin/env python
# encoding: utf-8

"""
@description: 时间转化为字符串

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec15_time_str.py
@time: 2016/12/25 14:08
"""

from datetime import datetime


def to_str():
    text = '2012-09-20'
    y = datetime.strptime(text, '%Y-%M-%d')
    z = datetime.now()
    print(z - y)

    now = datetime.now()
    print(now)

    formatted = datetime.strftime(now, '%H:%M:%S %Y-%m-%d')
    print(formatted)


def parse_ymd(s):
    year, month, day = s.split('-')
    return datetime(int(year), int(month), int(day))


def main():
    to_str()


if __name__ == '__main__':
    main()
