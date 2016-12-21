#!/usr/bin/env python
# encoding: utf-8

"""
@description:统计总数

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec12_count_sum.py
@time: 2016/12/7 23:14
"""

from collections import Counter

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]

morewords = ['why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes']


def count_sum():
    word_counts = Counter(words)
    top_three = word_counts.most_common(3)
    print(top_three)

    word_counts.update(morewords)


def update_count():
    a = Counter(words)
    b = Counter(morewords)

    c = a + b
    d = a - b

    print(c)
    print(d)


def main():
    count_sum()
    update_count()


if __name__ == '__main__':
    main()
