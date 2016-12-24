#!/usr/bin/env python
# encoding: utf-8

"""
@description: 正则中使用unicode

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec09_re_unicode.py
@time: 2016/12/24 14:19
"""

import re


def re_unicode():
    num = re.compile('\d+')
    print(num.findall('123'))
    # ariabic digits
    print(num.findall('\u0661\u0662\u0663'))

    # 匹配unicode 区间范围
    ariabic = re.compile('[\u0600-\u06ff\u0750-\u077f\u08a0-\u08ff]')


# 大小写的情况，并不是说ignore大小写就能匹配到的
def case_case():
    pat = re.compile('stra\u00dfe', re.I)
    s = 'straße'
    print(pat.match(s))
    print(pat.match(s.upper()))
    print(s.upper())


def main():
    # re_unicode()
    case_case()


if __name__ == '__main__':
    main()
