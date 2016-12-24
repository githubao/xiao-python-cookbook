#!/usr/bin/env python
# encoding: utf-8

"""
@description: 正则表达式 多行匹配

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec08_pattern_multiline.py
@time: 2016/12/24 13:44
"""

import re


def multi_line_match():
    comment = re.compile(r'/\*(.*?)\*/')
    text1 = '/* this is a comment */'
    text2 = """/* this is a
     multiline comment */"""

    print(comment.findall(text1))
    print(comment.findall(text2))

    comment2 = re.compile(r'/\*((?:.|\n)*?)\*/')
    print(comment2.findall(text1))
    print(comment2.findall(text2))

    comment3 = re.compile(r'/\*(.*I.*?)\*/', flags=re.DOTALL | re.IGNORECASE)
    print(comment3.findall(text1))
    print(comment3.findall(text2))


def main():
    multi_line_match()


if __name__ == '__main__':
    main()
