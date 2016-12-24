#!/usr/bin/env python
# encoding: utf-8

"""
@description: 正则表达式最短匹配

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec07_pattern_shortest.py
@time: 2016/12/24 13:40
"""

import re


def short_match():
    str_pat = re.compile(r'\"(.*)\"')
    str_pat2 = re.compile(r'\"(.*?)\"')
    text1 = 'Computer says "no."'
    text2 = 'Computer says "no." Phone says "yes".'

    print(str_pat.findall(text1))
    print(str_pat.findall(text2))
    print(str_pat2.findall(text1))
    print(str_pat2.findall(text2))

def main():
    short_match()


if __name__ == '__main__':
    main()
