#!/usr/bin/env python
# encoding: utf-8

"""
@description: 官方的线程池实现

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: py_threadpool.py
@time: 2016/12/21 12:27
"""

import os
import time

import threadpool
import urllib3

from xiaocook.chapter00.my_threadpool import download_file, urls


def multi_down():
    pool_size = 2
    pool = threadpool.ThreadPool(pool_size)
    requests = threadpool.makeRequests(download_file, urls)
    for req in requests:
        pool.putRequest(req)

    print('putting request to pool')
    pool.putRequest(threadpool.WorkRequest(download_file, args=('http://www.so.com',)))

    pool.poll()
    pool.wait()

    print("destroy all threads before exist")
    # pool.dismissedWorkers(pool_size, do_join=True)


def main():
    multi_down()


if __name__ == '__main__':
    main()
