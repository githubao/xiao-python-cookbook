#!/usr/bin/env python
# encoding: utf-8

"""
@description: 输出警告信息

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec11_warning.py
@time: 2017/4/11 21:50
"""

import warnings


def func(x, y, logfile=None, debug=False):
    warnings.simplefilter('always')
    warnings.simplefilter('error')
    # warnings.simplefilter('ignore')

    if logfile is not None:
        warnings.warn('logfile argument deprecated', DeprecationWarning)

    # warnings.warn('', UserWarning, SyntaxWarning, RuntimeWarning, ResourceWarning, FutureWarning)


def main():
    func(1, 2, '333')


if __name__ == '__main__':
    main()
