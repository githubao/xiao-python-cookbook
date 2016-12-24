#!/usr/bin/env python
# encoding: utf-8

"""
@description: 正则表达式替换

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec05_pattern_replace.py
@time: 2016/12/24 11:45
"""

import re
from calendar import month_abbr

datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'

def using_str_replace():
    text = 'yeah, but no, but yeah, but no, but yeah'
    print(text.replace('yeah','yep'))


def using_sub():
    text_subed = re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)
    print(text_subed)

    text_subed2 = datepat.sub(r'\3-\1-\2', text)
    print(text_subed2)


def using_sub_recall():
    def change_date(m):
        mon_name = month_abbr[int(m.group(1))]
        return '{} {} {}'.format(m.group(2), mon_name, m.group(3))

    text_subed3 = datepat.sub(change_date, text)
    print(text_subed3)

    # 发生了几次替换
    text_subed4, cnt = datepat.subn(change_date, text)
    print(text_subed4)
    print(cnt)


def main():
    using_str_replace()
    using_sub()
    using_sub_recall()


if __name__ == '__main__':
    main()
