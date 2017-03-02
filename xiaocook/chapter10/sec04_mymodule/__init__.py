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
@file: __init__.py.py
@time: 2017/3/2 20:47
"""


# from .a import A
# from .b import B

# 延迟加载
def A():
    from .a import A
    return A()


def B():
    from .b import B
    return B()
