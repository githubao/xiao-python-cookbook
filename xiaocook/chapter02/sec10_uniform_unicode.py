#!/usr/bin/env python
# encoding: utf-8

"""
@description: 使用unicode，统一的文本表示

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec10_uniform_unicode.py
@time: 2016/12/24 14:08
"""

import unicodedata

s1 = 'Spicy Jalape\u00f1o'
s2 = 'Spicy Jalapen\u0303o'

def uniform_str():
    print(s1)
    print(s2)
    print(s1 == s2)
    print(len(s1))
    print(len(s2))

def using_unicodedata():
    # 字符串整体组成
    t1 = unicodedata.normalize('NFC',s1)
    t2 = unicodedata.normalize('NFC',s2)

    print(t1)
    print(t2)
    print(t1==t2)
    print(ascii(t1))

    print("*"*20)

    # 字符串分开组成
    t3 = unicodedata.normalize('NFD',s1)
    t4 = unicodedata.normalize('NFD',s2)

    print(t3)
    print(t4)
    print(t3==t4)
    print(ascii(t3))

# 文本处理和过滤
# 判断是否为和音字符(上面的小波浪号)
def unicode_filter():
    t1 = unicodedata.normalize('NFD',s1)
    print(''.join(c for c in t1 if not unicodedata.combining(c)))

def main():
    # uniform_str()
    # using_unicodedata()
    unicode_filter()


if __name__ == '__main__':
    main()
