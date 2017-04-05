#!/usr/bin/env python
# encoding: utf-8

"""
@description: find file

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec09_findfile.py
@time: 2017/4/4 22:33
"""

import os
import time


def findfile(start, name):
    for relpath, dirs, files in os.walk(start):
        if name in files:
            full_path = os.path.join(start, relpath, name)
            print(os.path.normpath(os.path.abspath(full_path)))


def modified_within(top, seconds):
    now = time.time()
    for path, dirs, files in os.walk(top):
        for name in files:
            fullpath = os.path.join(path, name)
            if os.path.exists(fullpath):
                mtime = os.path.getmtime(fullpath)
                if mtime > (now - seconds):
                    print(fullpath)


def main():
    # findfile('D://code/NLP_Python', 'app.bat')
    modified_within('D://code/NLP_Python', 3600)


if __name__ == '__main__':
    main()
