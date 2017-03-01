#!/usr/bin/env python
# encoding: utf-8

"""
@description: 类功能混入maxin

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec18_maxin.py
@time: 2017/3/1 19:51
"""

from collections import defaultdict


class LoggedMappingMaxIn:
    __slot__ = ()

    def __getitem__(self, item):
        print('getting...')
        return super().__getitem__(item)

    def __setitem__(self, key, value):
        print('setting...')
        return super().__setitem__(key, value)

    def __delitem__(self, key):
        print('deleting...')
        return super().__delitem__(key)


class SetOnceMappingMaxIn:
    __slot__ = ()

    def __setitem__(self, key, value):
        if key in self:
            raise KeyError('{} already set'.format(key))
        return super().__setitem__(key, value)


class StringKeysMappingMaxIn:
    __slot__ = ()

    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise TypeError('key must be strings')
        return super().__setitem__(key, value)


def LoggedMapping(cls):
    cls_getitem = cls.__getitem__
    cls_setitem = cls.__setitem__
    cls_delitem = cls.__delitem__

    def __getitem__(self, item):
        print('getting...')
        return cls_getitem(self, item)

    def __setitem__(self, key, value):
        print('setting...')
        return cls_setitem(self, key, value)

    def __delitem__(self, key):
        print('deleting...')
        return cls_delitem(self, key)

    cls.__getitem__ = __getitem__
    cls.__setitem__ = __setitem__
    cls.__delitem__ = __delitem__

    return cls

class LoggedDict(LoggedMappingMaxIn, dict):
    pass

@LoggedMapping
class LoggedDict2(dict):
    pass


class SetOnceDefaultDict(SetOnceMappingMaxIn, defaultdict):
    pass


def demo():
    d = LoggedDict2()
    d['x'] = 23

    a = SetOnceDefaultDict(int)
    a['x'] = 3
    a['x'] = 2


def main():
    demo()


if __name__ == '__main__':
    main()
