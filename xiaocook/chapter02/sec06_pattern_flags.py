#!/usr/bin/env python
# encoding: utf-8

"""
@description: 正则表达式模式

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec06_pattern_flags.py
@time: 2016/12/24 11:28
"""

import re

text = 'UPPER PYTHON, lower python, Mixed Python'


def using_re_flags():
    found = re.findall('python', text, flags=re.IGNORECASE)
    print(found)

    subed = re.sub('python', 'snake', text, flags=re.IGNORECASE)
    print(subed)

    subed2 = re.sub('python', match_case('snake'), text, flags=re.IGNORECASE)
    print(subed2)


def match_case(word):
    def replace(m):
        s = m.group()
        if s.isupper():
            return word.upper()
        if s.islower():
            return word.lower()
        if s[0].isupper():
            return word.capitalize()
    return replace


def main():
    using_re_flags()


if __name__ == '__main__':
    main()
