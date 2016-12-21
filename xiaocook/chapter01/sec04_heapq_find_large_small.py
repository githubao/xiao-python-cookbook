#!/usr/bin/env python
# encoding: utf-8

"""
@description: 找到集合中的最大元素最小元素

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec04_heapq_find_large_small.py
@time: 2016/12/7 13:17
"""

import heapq


def heapq_demo():
    nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
    print(heapq.nlargest(3, nums))
    print(heapq.nsmallest(3, nums))


def heapq_max_min():
    portfolio = [
        {'name': 'IBM', 'shares': 100, 'price': 91.1},
        {'name': 'AAPL', 'shares': 50, 'price': 543.22},
        {'name': 'FB', 'shares': 200, 'price': 21.09},
        {'name': 'HPQ', 'shares': 35, 'price': 31.75},
        {'name': 'YHOO', 'shares': 45, 'price': 16.35},
        {'name': 'ACME', 'shares': 75, 'price': 115.85},
    ]

    cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
    expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])

    print(cheap)
    print(expensive)


def demo2():
    nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
    heapq.heapify(nums)
    print(nums)

    print(heapq.heappop(nums))
    print(heapq.heappop(nums))
    print(heapq.heappop(nums))


def main():
    # heapq_demo()
    # heapq_max_min()
    demo2()


if __name__ == '__main__':
    main()
