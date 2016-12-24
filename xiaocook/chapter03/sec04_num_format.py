#!/usr/bin/env python
# encoding: utf-8

"""
@description: 格式化数字

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec04_num_format.py
@time: 2016/12/24 22:15
"""

'''
一般形式： [<>^]? width [,]? (.digits)?
'''


def num_formatter():
    x = 1234.56789
    print(format(x, '0.2f'))
    print(format(x, '>10.1f'))
    print(format(x, '<10.1f'))
    print(format(x, ','))
    print(format(x, '0,.1f'))

    print(format(x, 'e'))
    print(format(x, '0.2E'))

    print('the value is {:0,.2f}'.format(x))

    # 修改千位分隔符为 '.'
    swap_separators = {ord('.'): ',', ord(','): '.'}
    print(format(x, ',').translate(swap_separators))


def main():
    num_formatter()


if __name__ == '__main__':
    main()
