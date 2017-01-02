#!/usr/bin/env python
# encoding: utf-8

"""
@description: 文件遍历

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec13_file_travel.py
@time: 2017/1/2 13:33
"""
import glob
import os
from fnmatch import fnmatch

from xiaocook.settings import FILE_PATH


def travel():
    names = os.listdir(FILE_PATH)
    print(names)

    files = [name for name in names if os.path.isfile(os.path.join(FILE_PATH, name))]
    print(files)

    texts = [name for name in names if name.endswith('txt')]
    print(texts)

    text_files = glob.glob('{}/*.txt'.format(FILE_PATH))
    print(text_files)

    html_files = [name for name in names if fnmatch(name, '*.html')]
    print(html_files)


def get_meta_data():
    html_files = [name for name in os.listdir(FILE_PATH) if fnmatch(name, '*.html')]
    print(html_files)

    name_sz_data = [
        (name, os.path.getsize(os.path.join(FILE_PATH, name)), os.path.getmtime(os.path.join(FILE_PATH, name))) for name
        in html_files]
    print(name_sz_data)

    print(list(os.stat(os.path.join(FILE_PATH, name)) for name in html_files))


def main():
    # travel()
    get_meta_data()


if __name__ == '__main__':
    main()
