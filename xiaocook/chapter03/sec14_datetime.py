#!/usr/bin/env python
# encoding: utf-8

"""
@description: 计算当前月份的日期范围

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec14_datetime.py
@time: 2016/12/25 13:48
"""

from datetime import datetime, date, timedelta
import calendar


def get_month_range(start_date=None):
    if not start_date:
        start_date = date.today().replace(day=1)
        _, days_in_month = calendar.monthrange(start_date.year, start_date.month)
        end_date = start_date + timedelta(days=days_in_month)
        return (start_date, end_date)


def month_iter():
    a_day = timedelta(days=1)
    first_day, last_day = get_month_range()
    while first_day < last_day:
        print(first_day)
        first_day += a_day


def month_generator():
    start = datetime(2016, 12, 1)
    stop = datetime(2017, 1, 1)
    step = timedelta(hours=8)
    for d in date_range(start, stop, step):
        print(d)


def date_range(start, stop, step):
    while start < stop:
        yield start
        start += step


def main():
    # month_iter()
    month_generator()


if __name__ == '__main__':
    main()
