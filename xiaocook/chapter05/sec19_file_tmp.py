#!/usr/bin/env python
# encoding: utf-8

"""
@description: 创建临时文件

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec19_file_tmp.py
@time: 2017/1/2 15:55
"""

from tempfile import TemporaryFile, NamedTemporaryFile
import tempfile


def temp():
    with TemporaryFile('w+b', encoding='utf-8') as f:
        f.write(b'111\n')
        f.write(b'test\n')

        f.seek(0)
        data = f.read()
        print(data)


def naming_temp():
    with NamedTemporaryFile('w+t', encoding='utf-8', delete=False) as f:
        print('file name is :', f.name)

    print(tempfile.gettempdir())

    f = NamedTemporaryFile(prefix='mytemp', suffix='.txt', dir='/mnt')
    print(f.name)


def main():
    # temp()
    naming_temp()


if __name__ == '__main__':
    main()
