#!/usr/bin/env python
# encoding: utf-8

"""
@description: 时间格式转换

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec12_time_field.py
@time: 2016/12/25 13:11
"""

from datetime import timedelta, datetime
from dateutil.relativedelta import relativedelta


def time_period():
    a = timedelta(days=2, hours=6)
    b = timedelta(hours=4.5)

    c = a + b
    print(c.days)

    # 一天之内的秒数
    print(c.seconds / 3600)
    # 所有的秒数
    print(c.total_seconds() / 3600)


def time_cal():
    a = datetime(2012, 9, 23)
    print(a + timedelta(days=10))

    b = datetime(2012, 12, 21)
    d = b - a
    print(d)
    print(d.days)

    now = datetime.today()
    print(now)


def leap_year():
    a = datetime(2012, 3, 1)
    b = datetime(2012, 2, 28)
    c = datetime(2013, 3, 1)
    d = datetime(2013, 2, 28)
    print(a - b)
    print(c - d)


def month_cal():
    a = datetime(2012, 9, 23)
    print(a + relativedelta(months=+1))
    print(a + relativedelta(months=+4))

    b = datetime(2012, 12, 21)
    print(b - a)

    d = relativedelta(b, a)
    print(d)
    print(d.months)
    print(d.days)


def main():
    # time_period()
    # time_cal()
    # leap_year()
    month_cal()


if __name__ == '__main__':
    main()
