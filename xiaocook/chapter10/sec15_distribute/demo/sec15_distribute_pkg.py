#!/usr/bin/env python
# encoding: utf-8

"""
@description: 分发包

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec15_distribute_pkg.py
@time: 2017/3/15 20:15
"""

'''
projectname
    README.txt
    Doc
        documentation.txt
    projectname
        __init__.py
        foo.py
        bar.py
        util
            __init__.py
            spam.py
            grok.py
    examples
        hello.py
'''


def main():
    print('python3 setup.py sdist')


if __name__ == '__main__':
    main()
