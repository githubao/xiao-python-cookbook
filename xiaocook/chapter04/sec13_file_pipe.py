#!/usr/bin/env python
# encoding: utf-8

"""
@description: 文件流 管道操作

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec13_file_pipe.py
@time: 2016/12/25 20:50
"""

import bz2
import fnmatch
import gzip
import os
import re

from xiaocook.settings import FILE_PATH


def gen_find(filepat, top):
    for path, dirlist, filelist in os.walk(top):
        for name in fnmatch.filter(filelist, filepat):
            yield os.path.join(path, name)


def gen_opener(filenames):
    for filename in filenames:
        if filename.endswith('.gz'):
            f = gzip.open(filename, 'r')
        elif filename.endswith('.bz2'):
            f = bz2.open(filename, 'r')
        else:
            f = open(filename, 'r')
        yield f
        f.close()


def gen_concatenate(iterators):
    for it in iterators:
        yield from it


def gen_grep(pattern, lines):
    pat = re.compile(pattern)
    for line in lines:
        if pat.search(line):
            yield line


# 遍历文件 打开文件 单个处理 正则匹配
def process_file():
    # lognames = gen_find('access-log*', 'www')
    lognames = gen_find('access-log*', FILE_PATH)
    files = gen_opener(lognames)
    lines = gen_concatenate(files)
    pylines = gen_grep('(?i)python', lines)
    # for line in pylines:
    #     print(line)

    bytecolumn = [line.rsplit(None, 1)[1] for line in pylines]
    bytes = [int(x) for x in bytecolumn if x != '-']
    print('Total', sum(bytes))


# 解析 读取实时数据 定时轮询
def main():
    process_file()


if __name__ == '__main__':
    main()
