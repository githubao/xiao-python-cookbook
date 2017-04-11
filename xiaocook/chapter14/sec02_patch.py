#!/usr/bin/env python
# encoding: utf-8

"""
@description: 给对象打补丁

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec02_patch.py
@time: 2017/4/11 20:26
"""

from  unittest.mock import patch, MagicMock
from xiaocook.chapter14 import example
import io
import unittest


@patch('xiaocook.chapter14.example.func1')
def test1(x, mock_func):
    example.func1(x)
    mock_func.assert_called_with(x)


def test2(x):
    with patch('xiaocook.chapter14.example.func1') as mock_func:
        example.func1(x)
        mock_func.assert_called_with(x)


def test3(x):
    p = patch('xiaocook.chapter14.example.fun1')
    mock_func = p.start()
    example.func1(x)
    mock_func.assert_called_with(x)
    p.stop()


x = 42


def test4():
    with patch('__main__.x', 32):
        print(x)


def test5():
    m = MagicMock(return_value=10)
    m(1, 2, debug=True)
    m.assert_called_with(1, 2, debug=True)
    # m.assert_called_with(1, 2)

    m.upper.return_value = 'HELLO'
    m.upper('helo')
    # assert m.upper.called

    # m.upper.assert_called_with('hello')


sample_data = io.BytesIO(b'''\
"IBM",91.1\r
"AA",13.25\r
"MSFT",27.72\r
    \r
    ''')


class Tests(unittest.TestCase):
    @patch('xiaocook.chapter14.example.urlopen', return_value=sample_data)
    def test_dowprices(self, mock_urlopen):
        p = example.downprices()
        self.assertTrue(mock_urlopen.called)
        self.assertEqual(p,
                         {'IBM': 91.1,
                          'AA': 13.25,
                          'MSFT': 27.72})


def main():
    # test1(4)
    # test4()
    # test5()

    unittest.main()


if __name__ == '__main__':
    main()
