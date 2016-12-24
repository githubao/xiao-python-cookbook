#!/usr/bin/env python
# encoding: utf-8

"""
@description: 浮点数精度

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec01_float_round.py
@time: 2016/12/24 19:16
"""


def round_demo():
    print(round(1.23, 1))
    print(round(1.27, 1))
    print(round(-1.23, 1))
    print(round(1.25361, 3))

    print(round(1.5,0))
    print(round(2.5,0))

    a = 1627731
    print(round(a,-1))
    print(round(a,-2))

    x=1.23456
    print(format(x,'0.2f'))
    print(format(x,'0.3f'))
    print('value is {:0.3f}'.format(x))



def main():
    round_demo()


if __name__ == '__main__':
    main()
