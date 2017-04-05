#!/usr/bin/env python
# encoding: utf-8

"""
@description: 读取配置文件

使用冒号或者等号都可以
键值不区分大小写
log_errors 的相同语义
可以读取多个文件并合并，相同的键，以最后一个的写入为准

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec10_cfg.py
@time: 2017/4/5 18:31
"""

from configparser import ConfigParser
from xiaocook.settings import FILE_PATH
import sys

file_name = '{}/simple.ini'.format(FILE_PATH)


def parser():
    cfg = ConfigParser()
    cfg.read(file_name)
    print(cfg.sections())
    print(cfg.get('installation', 'library'))
    print(cfg.getboolean('debug', 'log_errors'))
    print(cfg.getint('server', 'port'))
    print(cfg.get('server', 'signature'))

    # 写文件
    cfg.set('server', 'port', '9000')
    # cfg.write(sys.stdout)
    # new_file = ''
    # with open(new_file,'w',encoding='utf-8') as fw:
    #     cfg.write(fw)


def demo():
    print('log_errors = True')
    print('log_errors = true')
    print('log_errors = Yes')
    print('log_errors = 1')


def main():
    parser()


if __name__ == '__main__':
    main()
