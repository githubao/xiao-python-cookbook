#!/usr/bin/env python
# encoding: utf-8

"""
@description: 创建归档文件

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec08_achieve.py
@time: 2017/4/4 22:05
"""

import shutil


def pack_unpack():
    if False:
        shutil.unpack_archive('Python-3.3.0.tgz')
        shutil.make_archive('py33', 'zip', 'Python-3.3.0')
    print(shutil.get_archive_formats())

    '''
    [('bztar', "bzip2'ed tar-file"), ('gztar', "gzip'ed tar-file"), ('tar', 'uncompressed tar file'), ('xztar', "xz'ed tar-file"), ('zip', 'ZIP file')]
    '''


def main():
    pack_unpack()


if __name__ == '__main__':
    main()
