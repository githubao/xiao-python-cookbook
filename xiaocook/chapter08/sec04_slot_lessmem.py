#!/usr/bin/env python
# encoding: utf-8

"""
@description: 类属性使用slot减少内存使用

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec04_slot_lessmem.py
@time: 2017/2/7 19:26
"""


class Date:
    __slots__ = ['year', 'month', 'day']
    # __slots__ = ('year', 'month', 'day')

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

        # def __str__(self):
        #     # return '{}-{}-{}'.format(self.year,self.month,self.day)
        #     return vars()


def main():
    date = Date(2012, 2, 5)
    print([item for item in dir(date) if not item.startswith('__')])
    date.e = 7
    print([item for item in dir(date) if not item.startswith('__')])


if __name__ == '__main__':
    main()
