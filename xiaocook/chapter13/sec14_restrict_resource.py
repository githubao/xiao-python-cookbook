#!/usr/bin/env python
# encoding: utf-8

"""
@description: linux环境下，限制程序系统资源的使用

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec14_restrict_resource.py
@time: 2017/4/5 20:01
"""

import signal
import os
import resource


def time_exceeded(signo, frame):
    print('Time is up!')
    raise SystemExit(-1)


def set_max_runtime(seconds):
    soft, hard = resource.getrlimit(resource.RLIMIT_CPU)
    resource.setlimit(resource.RLIMIT_CPU, (seconds, hard))
    signal.signal(signal.SIGXCPU, time_exceeded)


def limit_memory(maxsize):
    soft, hard = resource.getrlimit(resource.RLIMIT_AS)
    resource.setlimit(resource.RLIMIT_AS, (maxsize, hard))


def main():
    set_max_runtime(15)
    while True:
        pass


if __name__ == '__main__':
    main()
