#!/usr/bin/env python
# encoding: utf-8

"""
@description: 重写format方法

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec02_rewrite_format.py
@time: 2017/1/8 16:13
"""

import time

_formats = {
    'ymd': '{d.year}-{d.month}-{d.day}',
    'mdy': '{d.month}/{d.day}/{d.year}',
    'dmy': '{d.day}/{d.month}/{d.year}',
}


class Date():
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __format__(self, format_spec):
        if format_spec == '':
            format_spec = 'ymd'
        fmt = _formats[format_spec]
        return fmt.format(d=self)


def fmt_demo():
    d = Date(2017, 1, 8)
    print(format(d))
    print(format(d, 'mdy'))
    print('today is {:dmy}'.format(d))


def fmt_time():
    s1 = '%Y-%m-%d %H:%M:%S'
    s2 = '%a %b %d %H:%M:%S %Y'

    print(time.strftime(s1,time.localtime()))
    print(time.strftime(s2,time.localtime()))

    print(time.mktime(time.strptime('2017-01-08 16:26:54',s1)))


def main():
    # fmt_demo()
    fmt_time()


if __name__ == '__main__':
    main()
