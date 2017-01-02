#!/usr/bin/env python
# encoding: utf-8

"""
@description: 压缩文件的读写

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec07_zip_io.py
@time: 2016/12/26 20:57
"""

import bz2
import gzip

from xiaocook.settings import FILE_PATH


def zip_io():
    with gzip.open(FILE_PATH + 'a.gz', 'wt', compresslevel=9) as f:
        f.write('a.gz')

    with gzip.open(FILE_PATH + 'a.gz', 'rt') as f:
        print(f.read())

    with bz2.open(FILE_PATH + 'b.bz2', 'w') as f:
        f.write(b'b.bz2')

    with bz2.open(FILE_PATH + 'b.bz2', 'r') as f:
        print(f.read())

    f = open(FILE_PATH + 'b.bz2', 'rb')
    with bz2.open(f, 'rt') as g:
        print(g.read())
    f.close()


def main():
    zip_io()


if __name__ == '__main__':
    main()
