#!/usr/bin/env python
# encoding: utf-8

"""
@description: sh 工具

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec07_shutil.py
@time: 2017/4/4 21:44
"""

import shutil
import os.path

src = ''
dst = ''


def demo():
    shutil.copy(src, dst)
    # preserve meta data
    shutil.copy2(src, dst)
    shutil.copytree(src, dst)
    shutil.copytree(src, dst, symlinks=True)
    shutil.move(src, dst)


def ignore_pyc_files(dirname, filenames):
    return [name for name in filenames if name.endswith('.pyc')]


def ignore_demo():
    # shutil.copytree(src, dst, ignore=ignore_pyc_files)
    shutil.copytree(src, dst, ignore=shutil.ignore_patterns('~', '.pyc'))


def path_demo():
    filename = '/Users/guido/programs/spam.py'
    print(os.path.basename(filename))
    print(os.path.dirname(filename))
    print(os.path.split(filename))
    print(os.path.join('/new/dir', os.path.basename(filename)))
    print(os.path.expanduser('~/guido/programs/spam.py'))


def copy_err():
    try:
        shutil.copytree(src, dst)
    except shutil.Error as e:
        for src, dst, msg in e.args[0]:
            print(dst, src, msg)


def main():
    path_demo()


if __name__ == '__main__':
    main()
