#!/usr/bin/env python
# encoding: utf-8

"""
@description: 令牌化字符串

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec18_str_tokenize.py
@time: 2016/12/24 16:58
"""

import re
from collections import namedtuple

text = 'foo = 23 + 42 * 10'
tokens = [('NAME', 'foo'), ('EQ', '='), ('NUM', '23'), ('PLUS', '+'),
          ('NUM', '42'), ('TIMES', '*'), ('NUM', '10')]

NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
TIMES = r'(?P<TIMES>\*)'
EQ = r'(?P<EQ>=)'
WS = r'(?P<WS>\s+)'

master_pat = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))


def tokenize():
    scanner = master_pat.scanner('foo = 42')

    while True:
        m = scanner.match()
        if not m:
            break

        print(m)
        print(m.lastgroup, m.group())


def generate_tokens(pat, text):
    Token = namedtuple('Token', ['type', 'value'])
    scanner = pat.scanner(text)
    for m in iter(scanner.match, None):
        yield Token(m.lastgroup, m.group())


def test_generate_tokens():
    for tok in generate_tokens(master_pat, 'foo = 42'):
        print(tok)


LT = r'(?P<LT><)'
LE = r'(?P<LE><=)'
EQ = r'(?P<EQ>=)'

another_pat = re.compile('|'.join([LE, LT, EQ]))


def match_str():
    PRINT = r'(?P<PRINT>print)'
    NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'

    master_pat = re.compile('|'.join([PRINT, NAME]))
    for tok in generate_tokens(master_pat, 'printer'):
        print(tok)


def main():
    # tokenize()
    # test_generate_tokens()
    match_str()


if __name__ == '__main__':
    main()
