#!/usr/bin/env python
# encoding: utf-8

"""
@description: 正则表达式匹配

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec04_pattern_match.py
@time: 2016/12/24 11:08
"""

import re


def using_str_func():
    text = 'yeah, but no, but yeah, but no, but yeah'
    print(text == 'yeah')
    print(text.startswith('yeah'))
    print(text.endswith('no'))
    print(text.find('no'))

datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
text1 = '11/27/2012'
text3 = '11/27/2012agfdh'
text2 = 'Nov 27, 2012'

def using_re():
    if re.match(r'\d+/\d+/\d+',text1):
        print('matched text1')
    else:
        print('no match text1')

    if re.match(r'\d+/\d+/\d+',text2):
        print('matched text2')
    else:
        print('no match text2')

    if datepat.match(text1):
        print('matched text1')
    else:
        print('no match text1')

    if datepat.match(text2):
        print('matched text2')
    else:
        print('no match text2')

    print(datepat.findall(text))

    m = datepat.match(text1)
    print(m)

    for index in range(m.lastindex+1):
        print(m.group(index))

    print(m.groups())

    matched = datepat.findall(text)
    print(matched)
    for month,day,year in datepat.findall(text):
        print('{}-{}-{}'.format(year, month, day))

    for m in datepat.finditer(text):
        print(m.groups())

    print('-'*20)
    datepat_exact = re.compile(r'(\d+)/(\d+)/(\d+)$')
    print(datepat_exact.match(text1))
    print(datepat_exact.match(text3))

def main():
    # using_str_func()
    using_re()


if __name__ == '__main__':
    main()
