#!/usr/bin/env python
# encoding: utf-8

"""
@description: 修改了代码之后，重新加载模块

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec06_reload.py
@time: 2017/3/2 21:05
"""

from xiaocook.chapter10 import sec01_init


def run_reload():
    sec01_init.spam()

    import importlib
    importlib.reload(sec01_init)

    sec01_init.spam()


def main():
    run_reload()


if __name__ == '__main__':
    main()
