#!/usr/bin/env python
# encoding: utf-8

"""
@description: 隐式的输入密码

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec04_getpass.py
@time: 2017/4/4 17:53
"""

import getpass


def svc_login(user, passwd):
    return 'admin' == user and '42' == passwd


def run():
    user = input('Enter your name: ')
    passwd = getpass.getpass('password: ')

    if svc_login(user, passwd):
        print('ok')
    else:
        print('failed')


def main():
    run()


if __name__ == '__main__':
    main()
