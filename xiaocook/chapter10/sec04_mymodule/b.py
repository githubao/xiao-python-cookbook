#!/usr/bin/env python
# encoding: utf-8

"""
@description:

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: b.py
@time: 2017/3/2 20:48
"""

from .a import A

class B(A):
    def bar(self):
        print('B bar')