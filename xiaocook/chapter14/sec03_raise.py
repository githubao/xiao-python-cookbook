#!/usr/bin/env python
# encoding: utf-8

"""
@description: 测试异常情况

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec03_raise.py
@time: 2017/4/11 21:04
"""

import unittest
import errno


def parse_int(s):
    return int(s)


class TestConversion(unittest.TestCase):
    def test_bad_int(self):
        # self.assertRaises(ValueError, parse_int, 'N/A')
        self.assertRaisesRegex(ValueError, 'invalid literal .*', parse_int, 'N/A')

    def test_bad_int2(self):
        with self.assertRaisesRegex(ValueError, 'invalid literal .*'):
            r = parse_int('N/A')

    class TestIO(unittest.TestCase):
        def test_file_not_found(self):
            try:
                f = open('/file/not/found')
            except IOError as e:
                self.assertEqual(e.errno, errno.ENOENT)
            else:
                self.fail('IOError not raised')

    def main():
        print("do sth")

    if __name__ == '__main__':
        main()
