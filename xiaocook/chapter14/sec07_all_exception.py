#!/usr/bin/env python
# encoding: utf-8

"""
@description: 捕获所有异常

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec07_all_exception.py
@time: 2017/4/11 21:37
"""

try:
    pass
except Exception as e:
    print(e)
except (SystemExit, KeyboardInterrupt, GeneratorExit) as e:
    print(e)


def main():
    print("do sth")


if __name__ == '__main__':
    main()
