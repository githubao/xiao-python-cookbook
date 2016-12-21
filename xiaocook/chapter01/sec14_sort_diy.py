#!/usr/bin/env python
# encoding: utf-8

"""
@description: 自定义比较操作

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec14_sort_diy.py
@time: 2016/12/9 19:47
"""

from operator import attrgetter


class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)


def sort_notCompare():
    users = [User(23), User(3), User(99)]
    print(users)
    print(sorted(users, key=lambda u: u.user_id))
    print(sorted(users, key=attrgetter('user_id')))


def main():
    sort_notCompare()


if __name__ == '__main__':
    main()
