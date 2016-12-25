#!/usr/bin/env python
# encoding: utf-8

"""
@description: 与星期相关的操作

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec13_weekdays.py
@time: 2016/12/25 13:40
"""

from datetime import datetime, timedelta

from dateutil.relativedelta import relativedelta
from dateutil.rrule import *

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
            'Friday', 'Saturday', 'Sunday']


def get_previous_byday(dayname, start_date=None):
    if start_date is None:
        start_date = datetime.today()

    day_num = start_date.weekday()
    day_num_target = weekdays.index(dayname)
    days_ago = (7 + day_num - day_num_target) % 7
    if days_ago == 0:
        days_ago = 7

    target_date = start_date - timedelta(days=days_ago)
    return target_date


def week_util():
    d = datetime.now()
    print(d)

    print(d + relativedelta(weekday=FR))
    print(d + relativedelta(weekday=FR(-1)))


def week():
    print(datetime.today())
    print(get_previous_byday('Monday'))
    print(get_previous_byday('Thursday'))


def main():
    # week()
    week_util()


if __name__ == '__main__':
    main()
