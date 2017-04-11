#!/usr/bin/env python
# encoding: utf-8

"""
@description: 创建自定义异常

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec08_define_except.py
@time: 2017/4/11 21:38
"""


class NetworkError(Exception):
    pass


class HostnameError(NetworkError):
    pass


class TimeoutError(NetworkError):
    pass


class ProtocolError(NetworkError):
    pass


try:
    pass
except TimeoutError:
    print('time out')
except ProtocolError:
    print('protocol err')


class CustomError(Exception):
    def __init__(self, message, status):
        super().__init__(message, status)
        self.message = message
        self.status = status


try:
    raise RuntimeError('it failed', 42, 'spam')
except RuntimeError as e:
    print(e.args)


def main():
    print("do sth")


if __name__ == '__main__':
    main()
