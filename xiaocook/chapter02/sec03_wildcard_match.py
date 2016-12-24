#!/usr/bin/env python
# encoding: utf-8

"""
@description:实现shell里面的通配符匹配

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec03_wildcard_match.py
@time: 2016/12/24 10:51
"""

from fnmatch import fnmatch,fnmatchcase

addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK'
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE'
]

def test_fnmatch():
    print(fnmatch('foo.txt','*.txt'))
    print(fnmatch('foo.txt','?oo.txt'))
    print(fnmatch('Dat45.csv','Dat[0-9]*'))

    names = ['Dat1.csv','Dat2.csv','config.ini','foo.py']
    matches = [name for name in names if fnmatch(name,'Dat*.csv')]
    print(matches)

    # 大小写不敏感
    print(fnmatch('foo.txt','*.TXT'))
    # 大小写敏感
    print(fnmatchcase('foo.txt','*.TXT'))

def process_str_with_fnmatch():
    print([addr for addr in addresses if fnmatchcase(addr,'* CLARK')])
    print([addr for addr in addresses if fnmatchcase(addr,'54[0-9][0-9] *CLARK*')])

def main():
    # test_fnmatch()
    process_str_with_fnmatch()


if __name__ == '__main__':
    main()

