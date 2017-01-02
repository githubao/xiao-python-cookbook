#!/usr/bin/env python
# encoding: utf-8

"""
@description: 与关系型数据库交互

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec08_sqlite3.py
@time: 2017/1/2 20:34
"""

from xiaocook.settings import FILE_PATH

file_name = '{}/test.db'.format(FILE_PATH)

stocks = [
    ('GOOG', 100, 490.1),
    ('AAPL', 50, 545.75),
    ('FB', 150, 7.45),
    ('HPQ', 75, 33.2),
]

import sqlite3


class SqlModule():
    def __init__(self):
        self.db = sqlite3.connect(file_name)

    def execute(self, sql):
        c = self.db.cursor()
        c.execute(sql)
        self.db.commit()

    def executemamy(self, sql, datas):
        c = self.db.cursor()
        c.executemany(sql, datas)
        self.db.commit()

    def select(self, sql):
        return self.db.execute(sql)

    def close(self):
        self.db.close()


def sql_demo():
    min_price = 100

    mysql = SqlModule()
    mysql.execute('create table portfolio (symbol text,shares integer,price real)')
    mysql.executemamy('insert into portfolio VALUES (?,?,?)', stocks)
    for row in mysql.select('select * from portfolio where price >= {}'.format(min_price)):
        print(row)


def main():
    sql_demo()


if __name__ == '__main__':
    main()
