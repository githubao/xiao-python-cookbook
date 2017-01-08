#!/usr/bin/env python
# encoding: utf-8

"""
@description: 数据配置

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: settings.py
@time: 2016/12/21 12:30
"""
import logging
from os.path import dirname, abspath

ROOT_PATH = dirname(abspath(__file__)) + '/'
FILE_PATH = ROOT_PATH + 'file/'

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    # filename='/mnt/work/nlptrain/logs/ml.log',
                    # filemode='a'
                    )