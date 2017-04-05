#!/usr/bin/env python
# encoding: utf-8

"""
@description: 启动一个web浏览器

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec15_webbrowser.py
@time: 2017/4/5 20:09
"""

import webbrowser


def run():
    webbrowser.open('https://www.python.org')


def run2():
    # ['windows-default', 'C:\\Program Files\\Internet Explorer\\IEXPLORE.EXE']
    print(webbrowser._tryorder)
    c = webbrowser.get('C:\\Program Files\\Internet Explorer\\IEXPLORE.EXE')
    c.open_new_tab('https://www.python.org')


def main():
    # run()
    run2()


if __name__ == '__main__':
    main()
