#!/usr/bin/env python
# encoding: utf-8

"""
@description: 序列化对象

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec21_file_serialize.py
@time: 2017/1/2 16:13
"""

import sys
import pickle

from xiaocook.settings import FILE_PATH

file_name = FILE_PATH+'serialized.txt'

import time
import threading

class CountDown:
    def __init__(self,n):
        self.n = n
        self.thr = threading.Thread(target=self.run)
        self.thr.daemon=True
        self.thr.start()

    def run(self):
        while self.n > 0:
            print('minus: ',self.n)
            self.n -= 1
            time.sleep(1)

    def __getstate__(self):
        return self.n

    def __setstate__(self,n):
        self.__init__(n)


def pickle_state():
    c = CountDown(10)
    time.sleep(4)
    f = open(file_name,'wb')
    pickle.dump(c,f)
    f.close()

    print('new---')

    f = open(file_name,'rb')
    pickle.load(f)

    time.sleep(10)



def serialize():
    data = {'1': True}

    with open(file_name, 'wb') as f:
        pickle.dump(data, f)

    s = pickle.dumps(data)
    print(s)

    with open(file_name, 'rb') as f:
        print(pickle.load(f))

    print(pickle.loads(s))


def main():
    # serialize()
    pickle_state()


if __name__ == '__main__':
    main()
