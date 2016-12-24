#!/usr/bin/env python
# encoding: utf-8

"""
@description: 使用正则 切分字符串

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec01_re_split.py
@time: 2016/12/12 14:41
"""

import re


def re_split():
    line = 'asdf fjdk; afed, fjek,asdf, foo'
    results = re.split(r'[;,\s]\s*', line)
    print(results)

    #包含分组
    fields = re.split(r'(;|,|\s)\s*',line)
    print(fields)

    values = fields[::2]
    delimiters = fields[1::2]+['']
    new_line=''.join(v+d for v,d in zip(values,delimiters))
    print(new_line)

    # 包含分组且非捕获
    fields_no_capture = re.split(r'(?:,|;|\s)\s*',line)
    print(fields_no_capture)


def main():
    re_split()


if __name__ == '__main__':
    main()
