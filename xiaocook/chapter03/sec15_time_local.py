#!/usr/bin/env python
# encoding: utf-8

"""
@description: 时间国际化

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec15_time_local.py
@time: 2016/12/25 14:17
"""

from datetime import datetime, timedelta
import pytz

d = datetime(2013, 3, 10, 1, 45, 0)

central = pytz.timezone('US/Central')
loc_d = central.localize(d)


def timezone_demo():
    print(loc_d)

    bang_d = loc_d.astimezone(pytz.timezone('Asia/Kolkata'))
    print(bang_d)


def summer_time():
    print(loc_d)

    # later = loc_d + timedelta(minutes=30)
    # print(later)

    later = central.normalize(loc_d + timedelta(minutes=30))
    print(later)


def utc_time():
    utf_d = loc_d.astimezone(pytz.utc)
    print(utf_d)

    print(pytz.common_timezones)


def main():
    # timezone_demo()
    # summer_time()
    utc_time()


if __name__ == '__main__':
    main()
