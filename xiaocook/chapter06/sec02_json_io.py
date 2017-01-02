#!/usr/bin/env python
# encoding: utf-8

"""
@description: 读写json数据
None bool int float str collection

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec02_json_io.py
@time: 2017/1/2 17:20
"""

import json
from xiaocook.settings import FILE_PATH
from pprint import pprint
from collections import OrderedDict

file_name = FILE_PATH + 'data.json'

data = {
    'name': 'ACME',
    'shares': 100,
    'price': 542.23,
    'bool': True
}


def rw():
    json_str = json.dumps(data)
    print(json_str)

    data2 = json.loads(json_str)
    print(data2)

    with open(file_name, 'w') as f:
        json.dump(data, f)

    with open(file_name, 'r') as f:
        print(json.load(f))

    pprint(data2)


def loads_with_data_structure():
    json_str = json.dumps(data, indent=2)
    print(json_str)

    # data2 = json.loads(json_str, object_pairs_hook=OrderedDict)
    # print(data2)

    data3 = json.loads(json_str, object_pairs_hook=JsonObject)
    print(data3.price)


class JsonObject():
    def __init__(self, d):
        self.__dict__ = {}
        for k, v in d:
            self.__dict__[k] = v


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y


classes = {
    'Point': Point
}


def serialize_instance(obj):
    d = {'__classname__': type(obj).__name__}
    d.update(vars(obj))
    return d


def unserialize_instance(d):
    clsname = d.pop('__classname__', None)
    if clsname:
        cls = classes[clsname]
        obj = cls.__new__(cls)
        for k, v in d.items():
            setattr(obj, k, v)
        return obj
    else:
        return d


def dump_obj():
    p = Point(2, 3)
    data = json.dumps(p, default=serialize_instance)
    print(data)

    p2 = json.loads(data, object_hook=unserialize_instance)
    print(p2.x, " ", p2.y)


def main():
    # rw()
    # loads_with_data_structure()
    dump_obj()


if __name__ == '__main__':
    main()
