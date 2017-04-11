#!/usr/bin/env python
# encoding: utf-8

"""
@description: 重定向测试输出

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec04_redirect.py
@time: 2017/4/11 21:13
"""

import unittest
import sys
from xiaocook.settings import FILE_PATH


class MyTest(unittest.TestCase):
    def test_hello(self):
        self.assertEqual('1', '2')


def run():
    unittest.main()


def redirect(out=sys.stderr, verbosity=2):
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(sys.modules[__name__])
    unittest.TextTestRunner(out, verbosity=verbosity).run(suite)


def run2():
    # redirect()
    with open('{}/testing.out'.format(FILE_PATH), 'w', encoding='utf-8') as f:
        redirect(f)


def main():
    # run()
    run2()


if __name__ == '__main__':
    main()
