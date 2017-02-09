#!/usr/bin/env python
# encoding: utf-8

"""
@description: 抽象类 或者 接口

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec12_abstract_class.py
@time: 2017/2/8 20:28
"""

from abc import ABCMeta, abstractmethod
import io
import collections


# abstractmethod 同样可以注释 属性方法 类方法 静态方法
class IStream(metaclass=ABCMeta):
    @abstractmethod
    def read(self, maxbytes=-1):
        pass

    @abstractmethod
    def write(self, data):
        pass


class SocketStream(IStream):
    def read(self, maxbytes=-1):
        pass

    def write(self, data):
        pass


def serialize(obj, stream):
    if not isinstance(stream, IStream):
        raise TypeError('Expected an IStream')
    pass


def collection_abcs():
    a = collections.Sequence
    b = collections.Iterable
    c = collections.Sized
    d = collections.Mapping


def register_demo():
    IStream.register(io.IOBase)

    f = open(__file__, encoding='utf-8')
    print(isinstance(f, IStream))


def main():
    register_demo()


if __name__ == '__main__':
    main()
