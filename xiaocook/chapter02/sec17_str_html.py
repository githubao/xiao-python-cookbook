#!/usr/bin/env python
# encoding: utf-8

"""
@description: 处理xml html

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec17_str_html.py
@time: 2016/12/24 16:45
"""

import html
from xml.sax import saxutils

s = 'Elements are written as "<tag>text</tag>"'


def html_processor():
    print(s)
    print(html.escape(s))
    print(html.escape(s, quote=False))


def html_processor2():
    s = 'Spicy Jalapeño'
    t = 'Spicy &quot;Jalape&#241;o&quot;'
    u = 'The prompt is &gt;&gt;&gt;'

    # 把非ascii字符编码到html里面
    print(s.encode('ascii', errors='xmlcharrefreplace'))

    # html 还原
    print(html.unescape(t))
    # xml还原
    print(saxutils.unescape(u))


def main():
    # html_processor()
    html_processor2()


if __name__ == '__main__':
    main()
