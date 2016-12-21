#!/usr/bin/env python
# encoding: utf-8

"""
@description: 解包装 可迭代对象

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec02_unpacking_iteratables.py
@time: 2016/12/6 22:43
"""
import math


def drop_first_last(grades):
    first, *middle, last = grades
    return sum(middle) / len(middle)


def avg_comparison(f1, f2):
    if f1 == f2:
        return 'equal'
    elif f1 < f2:
        return 'bigger'
    else:
        return 'smaller'


def unpack_iteraterables():
    record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
    (name, email, *phone_numbers) = record
    print(name)
    print(phone_numbers)

    sales_record = [10, 8, 7, 1, 9, 5, 10, 3]
    *trailing_qtrs, current_qtr = sales_record
    print(trailing_qtrs)
    print(current_qtr)

    trailing_avg = sum(trailing_qtrs) / len(trailing_qtrs)
    print(avg_comparison(trailing_avg, current_qtr))


def demo2():
    records = [
        ('foo', 1, 2),
        ('bar', 'hello'),
        ('foo', 3, 4),
    ]

    def do_foo(x, y):
        print('foo', x, y)

    def do_bar(s):
        print('bar', s)

    for tag, *args in records:
        if tag == 'foo':
            do_foo(*args)
        elif tag == 'bar':
            do_bar(*args)


def demo3():
    line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
    uname, *fileds, homedir, sh = line.split(':')
    print(uname)
    print(homedir)
    print(sh)


def demo4():
    data = ['ACME', 50, 123.45, (12, 18, 2012)]
    (name, *_, (*_, year)) = data
    print(name)
    print(year)


def demo5():
    items = [1, 10, 7, 4, 5, 9]
    head, *tail = items
    print(head)
    print(tail)

def demo6():
    items = [1, 10, 7, 4, 5, 9]

    def sum(items):
        head,*tail = items
        return head + sum(tail) if tail else head

    print(sum(items))

def main():
    # unpack_iteraterables()
    # demo2()
    # demo3()
    # demo4()
    demo5()
    demo6()


if __name__ == '__main__':
    main()
