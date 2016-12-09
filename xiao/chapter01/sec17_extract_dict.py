#!/usr/bin/env python
# encoding: utf-8

"""
@description: 从原始字典构建符合条件的字典

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec17_extract_dict.py
@time: 2016/12/9 20:17
"""

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75,
}


def build_dict():
    p1 = {key: value for key, value in prices.items() if value > 200}
    print(p1)
    tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
    p2 = {key: value for key, value in prices.items() if key in tech_names}
    print(p2)
    p3 = {key: prices[key] for key in prices.keys() & tech_names}
    print(p3)


def main():
    build_dict()


if __name__ == '__main__':
    main()
