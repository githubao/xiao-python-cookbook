#!/usr/bin/env python
# encoding: utf-8

"""
@description: 处理多个异常

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec06_handle_except.py
@time: 2017/4/11 21:26
"""

import errno


def demo1():
    try:
        pass
    except (ValueError, FileExistsError) as e:
        print('err')

    try:
        f = open('file')
    except OSError as e:
        if e.errno == errno.ENOENT:
            print('File not found')
        elif e.errno == errno.EACCES:
            print('Permission denied')
        else:
            print('Unexpected error: %d'.format(e.errno))


def main():
    # (<class 'FileExistsError'>, <class 'OSError'>, <class 'Exception'>, <class 'BaseException'>, <class 'object'>)
    print(FileExistsError.__mro__)


if __name__ == '__main__':
    main()
