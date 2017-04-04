#!/usr/bin/env python
# encoding: utf-8

"""
@description: 解析命令行选项

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec03_args_parse.py
@time: 2017/4/4 17:26
"""

'''
python sec03_args_parse.py -h

usage: sec03_args_parse.py [-h] -p pattern [-v] [--speed {slow,fast}]
                           [filename [filename ...]]

Search some files

positional arguments:
  filename

optional arguments:
  -h, --help            show this help message and exit
  -p pattern, --pat pattern
                        text pattern to search for
  -v                    verbose mode
  --speed {slow,fast}   output file


'''

import argparse

parser = argparse.ArgumentParser(description='Search some files')
parser.add_argument(dest='filenames', metavar='filename', nargs='*')
parser.add_argument('-p', '--pat', metavar='pattern', required=True, dest='patterns', action='append',
                    help='text pattern to search for')
parser.add_argument('-v', dest='verbose', action='store_true', help='verbose mode')
parser.add_argument('-o', dest='outfile', action='store', help='output file')
parser.add_argument('--speed', dest='speed', action='store', choices={'slow', 'fast'}, default='slow',
                    help='search speed')

args = parser.parse_args()

print(args)

for key, value in args.__dict__.items():
    print('{}:{}'.format(key, value))


def main():
    print('python sec03_args_parse.py -v -p spam --pat=eggs foo.txt bar.txt -o results.txt --speed=fast')

    'action store store_true append'


if __name__ == '__main__':
    main()
