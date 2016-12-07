#!/usr/bin/env python
# encoding: utf-8

"""
@description: 求字典的最大值 最小值

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec08_zip_and_lambda.py
@time: 2016/12/7 20:52
"""

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75,
}


def max_dict():
    min_price_key = min(prices, key=lambda k: prices[k])
    print(min_price_key)

    min_price = min(zip(prices.values(), prices.keys()))
    max_price = max(zip(prices.values(), prices.keys()))
    print(min_price)
    print(max_price)

    sorted_prices = sorted(zip(prices.values(), prices.keys()))
    print(sorted_prices)


def main():
    max_dict()


if __name__ == '__main__':
    main()
