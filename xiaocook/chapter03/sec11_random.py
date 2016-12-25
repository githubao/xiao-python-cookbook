#!/usr/bin/env python
# encoding: utf-8

"""
@description: 随机数

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec11_random.py
@time: 2016/12/25 13:03
"""

import random
import time
import ssl


def rand():
    random.seed(time.time())

    values = [1, 2, 3, 4, 5, 6]
    for _ in range(3):
        print(random.choice(values))

    for _ in range(3):
        print(random.sample(values, 3))

    for _ in range(3):
        random.shuffle(values)
        print(values)

    for _ in range(3):
        print(random.randint(0, 10))

    for _ in range(3):
        print(random.random())

    print(random.getrandbits(200))

    print('*' * 20)
    print(ssl.RAND_bytes(20))


def distribute_rand():
    # 基于均匀分布的随机数
    for _ in range(3):
        print(random.uniform(0, 1))

    # 基于高斯分布的随机数
    for _ in range(3):
        print(random.gauss(0, 1))


def main():
    rand()
    distribute_rand()


if __name__ == '__main__':
    main()
