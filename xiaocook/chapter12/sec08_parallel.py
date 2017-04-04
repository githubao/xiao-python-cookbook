#!/usr/bin/env python
# encoding: utf-8

"""
@description: 并发编程

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec08_parallel.py
@time: 2017/4/4 12:41
"""

import gzip
import io
import glob
from concurrent import futures


def find_robots(filename):
    robots = set()
    with gzip.open(filename) as f:
        for line in io.TextIOWrapper(f, encoding='ascii'):
            fields = line.split()
            if fields[6] == 'robots.txt':
                robots.add(fields[0])
    return robots


def find_all_robots(logdir):
    files = glob.glob(logdir + '/*.log.gz')
    all_robots = set()
    for robots in map(find_robots, files):
        all_robots.update(robots)
    return all_robots


def find_all_robots2(logdir):
    files = glob.glob(logdir + '/*.log.gz')
    all_robots = set()
    # 使用核CPU，创建多个Python独立的解释器，执行任务
    with futures.ProcessPoolExecutor() as poll:
        for robots in poll.map(find_robots, files):
            all_robots.update(robots)
    return all_robots


def pool_execute():
    def work(x):
        return 'sth'

    datas = []
    data = ''

    # 多条提交
    with futures.ProcessPoolExecutor() as pool:
        results = pool.map(work, datas)

    # 单条提交
    with futures.ProcessPoolExecutor() as pool:
        future_result = pool.submit(work, data)
        res = future_result.result()
        print(res)

    def when_done(r):
        print('Got: ', r.result())

    # 防止阻塞，添加回调函数
    with futures.ProcessPoolExecutor() as pool:
        future_result = pool.submit(work, data)
        future_result.add_done_callback(when_done)


def map_reduce():
    robots = find_all_robots('logs')
    for ipaddr in robots:
        print(ipaddr)


def main():
    print("do sth")


if __name__ == '__main__':
    main()
