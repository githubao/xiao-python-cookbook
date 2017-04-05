#!/usr/bin/env python
# encoding: utf-8

"""
@description: 测试stdout的输出

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec01_stdout_test.py
@time: 2017/4/5 20:21
"""

from io import StringIO
from unittest import TestCase
from unittest.mock import patch


def urlprint(protocol, host, domain):
    url = '{}://{}.{}'.format(protocol, host, domain)
    print(url)


class TestUrlPrint(TestCase):
    def test_url_gets_to_stdout(self):
        protocol = 'http'
        host = 'www'
        domain = 'example.com'
        expected_url = '{}://{}.{}\n'.format(protocol, host, domain)

        with patch('sys.stdout', new=StringIO()) as fake_out:
            urlprint(protocol, host, domain)
            self.assertEqual(fake_out.getvalue(), expected_url)


def main():
    print("do sth")


if __name__ == '__main__':
    main()
