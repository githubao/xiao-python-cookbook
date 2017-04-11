#!/usr/bin/env python
# encoding: utf-8

"""
@description: 自动忽略异常或者失败

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec05_ignore_except.py
@time: 2017/4/11 21:20
"""

import unittest
import os
import platform


class Tests(unittest.TestCase):
    def test_0(self):
        self.assertTrue(True)

    @unittest.skip('skipped test')
    def test_1(self):
        self.fail('should have failed')

    @unittest.skipIf(os.name == 'posix', 'Not supported in Unix')
    def test_2(self):
        import winreg

    @unittest.skipUnless(platform.system() == 'Darwin', 'Mac specific test')
    def test_3(self):
        self.assertTrue(True)

    @unittest.expectedFailure
    def test_4(self):
        self.assertEqual(2 + 2, 5)


def main():
    print("do sth")


if __name__ == '__main__':
    main()
