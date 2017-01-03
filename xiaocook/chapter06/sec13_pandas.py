#!/usr/bin/env python
# encoding: utf-8

"""
@description: 使用pandas 处理csv数据

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec13_pandas.py
@time: 2017/1/3 22:24
"""

import pandas
from xiaocook.settings import FILE_PATH

file_name = '{}/rats.csv'.format(FILE_PATH)


def pandas_demo():
    rats = pandas.read_csv(file_name, skip_footer=1)
    print(rats,end='\n\n\n')

    print(rats['ZIP Code'].unique(),end='\n\n\n')

    crew_dispatched = rats[rats['ZIP Code'] == 60609]
    print(crew_dispatched,end='\n\n\n')

    print(crew_dispatched['ZIP Code'].value_counts()[:3],end='\n\n\n')

    dates = crew_dispatched.groupby('Creation Date')
    date_counts = dates.size()
    print(date_counts,end='\n\n\n')

    date_counts.sort_values()
    print(date_counts,end='\n\n\n')


def main():
    pandas_demo()


if __name__ == '__main__':
    main()
