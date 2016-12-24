#!/usr/bin/env python
# encoding: utf-8

"""
@description: 判断字符串是否以另一个字符串开头或者结尾

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec02_multi_endwith.py
@time: 2016/12/24 10:38
"""

import os
from urllib.request import urlopen
import re

def multi_end():
    filenames = os.listdir('.')
    print(filenames)
    code_file = [name for name in filenames if name.endswith(('.py', '.sh'))]
    print(code_file)

    if any(name.endswith(('.py', '.sh')) for name in filenames):
        print('exists py or sh file')


def re_end():
    url = 'http://www.python.org'
    m = re.match('http:|https:|ftp:',url)
    if m:
        print(m.group())


def multi_open(name):
    if name.startswith(('http:', 'https:', 'ftp:')):
        return urlopen(name).read()
    else:
        with open(name,encoding='utf-8') as f:
            return f.read()

def test_multi_open():
    file_name = __file__
    url_name = 'http://www.baidu.com'

    print(multi_open(file_name))
    print(multi_open(url_name))

def main():
    multi_end()
    re_end()
    # test_multi_open()


if __name__ == '__main__':
    main()
