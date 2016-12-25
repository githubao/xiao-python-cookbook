#!/usr/bin/env python
# encoding: utf-8

"""
@description: 手动遍历可迭代对象

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec01_iter_next.py
@time: 2016/12/25 14:33
"""


def manual_iter():
    with open(__file__, encoding='utf-8') as f:
        try:
            while True:
                line = next(f)
                print(line.strip('\n'))
        except StopIteration as e:
            print(e.value)


def manual_iter2():
    with open(__file__, encoding='utf-8') as f:
        while True:
            line = next(f, None)
            if not line:
                break
            print(line.strip('\n'))


def iter_concept():
    items = [1, 2, 3]

    it = iter(items)
    print(next(it))
    print(next(it))
    print(next(it))
    print(next(it))


def main():
    # manual_iter()
    # manual_iter2()
    iter_concept()


if __name__ == '__main__':
    main()
