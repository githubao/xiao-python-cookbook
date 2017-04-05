#!/usr/bin/env python
# encoding: utf-8

"""
@description: 独立的log配置文件的添加

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec12_depend_log.py
@time: 2017/4/5 19:45
"""

import logging

logger = logging.getLogger(__name__)
logger.level = logging.INFO
logger.addHandler(logging.NullHandler())


def log():
    logger.info('some msg')
    logging.basicConfig()
    logger.info('other msg')
    logger.level = logging.ERROR
    logger.info('info msg')


def main():
    log()


if __name__ == '__main__':
    main()
