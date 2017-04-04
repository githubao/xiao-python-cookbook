#!/usr/bin/env python
# encoding: utf-8

"""
@description: 文件输入输出重定向

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec01_redirect_file.py
@time: 2017/4/4 17:16
"""

import fileinput

'''
$ ll | python sec01_redirect_file.py
Magic: total 2
Magic: -rwxr-xr-x 1 BaoQiang 197121 274 三月 15 20:28 __init__.py*
Magic: -rwxr-xr-x 1 BaoQiang 197121 506 四月  4 17:19 sec01_redirect_file.py*
'''


def read_file():
    with fileinput.input(__file__, openhook=fileinput.hook_encoded('utf-8')) as f:
        for line in f:
            # print(f.filename(), f.lineno(), line)
            print('{}: '.format(f.lineno()), line, end='')


def main():
    with fileinput.input() as f_input:
        for line in f_input:
            print('Magic: {}'.format(line), end='')


if __name__ == '__main__':
    # main()
    read_file()
