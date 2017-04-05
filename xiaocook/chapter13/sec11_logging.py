#!/usr/bin/env python
# encoding: utf-8

"""
@description: 记录日志

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec11_logging.py
@time: 2017/4/5 18:44
"""

import logging
import logging.config

# logging.basicConfig(
#         filename='../file/app.log',
#         level=logging.ERROR,
#         format='%(levelname)s:%(asctime)s:%(message)s'
# )

# 使用文件配置
logging.config.fileConfig('../file/logconfig.ini')

logging.getLogger().level = logging.DEBUG


def log():
    hostname = 'www.python.org'
    item = 'spam'
    filename = 'data.csv'
    mode = 'r'

    logging.critical('Host {} unknown'.format(hostname))
    logging.error('Could not find {}'.format(item))
    logging.warning('Feature is deprecated')
    logging.info('Opening file {!r}, mode={!r}'.format(filename, mode))
    logging.debug('Got here')


def main():
    log()


if __name__ == '__main__':
    main()
