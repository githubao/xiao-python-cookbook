#!/usr/bin/env python
# encoding: utf-8

"""
@description: 清洗字符串

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec12_str_clean.py
@time: 2016/12/24 15:00
"""

import unicodedata
import sys

remap = {
    ord('\t'): ' ',
    ord('\f'): ' ',
    ord('\r'): None
}

cmb_chars = dict.fromkeys(c for c in range(sys.maxunicode)
                          if unicodedata.combining(chr(c)))


# upper lower replace sub normalize
def clean():
    s = 'pýtĥöñ\fis\tawesome\r\n'
    print(s)

    a = s.translate(remap)
    print(a)

    b = unicodedata.normalize('NFD', a)
    c = b.translate(cmb_chars)
    print(c)


def arabic_to_num():
    digitmap = {c: ord('0') + unicodedata.digit(chr(c))
                for c in range(sys.maxunicode)
                if unicodedata.category(chr(c)) == 'Nd'}

    print(len(digitmap))
    x = '\u0661\u0662\u0663'
    print(x.translate(digitmap))


def test():
    print(chr(65))
    print(ord('A'))


def use_codes_to_clean():
    a = 'pýtĥöñ is awesome\n'
    b = unicodedata.normalize('NFD', a)
    rm_no_ascii = b.encode('ascii', 'ignore').decode('ascii')
    print(rm_no_ascii)


def main():
    # clean_str()
    # test()
    # arabic_to_num()
    use_codes_to_clean()


if __name__ == '__main__':
    main()
