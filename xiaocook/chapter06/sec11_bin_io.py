#!/usr/bin/env python
# encoding: utf-8

"""
@description: 二进制文件的读写

< 低位在前
> 高位在前
! 网络字节顺序
i 32位整数
d 64位浮点数
f 32位浮点数

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec11_bin_io.py
@time: 2017/1/2 21:01
"""

from struct import Struct
from xiaocook.settings import FILE_PATH

from collections import namedtuple
import numpy as np

file_name = '{}/struct.bin'.format(FILE_PATH)


def write_records(records, format, f):
    record_struct = Struct(format)
    for r in records:
        f.write(record_struct.pack(*r))


def read_records(format, f):
    record_struct = Struct(format)
    chunks = iter(lambda: f.read(record_struct.size), b'')
    return (record_struct.unpack(chunk) for chunk in chunks)


def unpack_records(format, data):
    record_struct = Struct(format)
    return (record_struct.unpack_from(data, offset) for offset in range(0, len(data), record_struct.size))


def using_struct():
    records = [(1, 2.3, 4.5),
               (6, 7.8, 9.0),
               (12, 13.4, 56.7)]

    with open(file_name, 'wb') as f:
        write_records(records, '<idd', f)

    with open(file_name, 'rb') as f:
        for rec in read_records('<idd', f):
            print(rec)

    with open(file_name, 'rb') as f:
        data = f.read()
        for rec in unpack_records('<idd', data):
            print(rec)


def using_numpy():
    struct = Struct('<idd')
    print(struct.pack(1, 2.1, 3.2))
    origin = struct.unpack(struct.pack(1, 2.1, 3.2))

    Record = namedtuple('Record', ['kind', 'x', 'y'])
    rec = Record(*origin)
    print(rec)

    with open(file_name, 'rb') as f:
        recs = np.fromfile(f, dtype='<i,<d,<d')
        print(recs)

        print(recs[1])


def main():
    # using_struct()
    using_numpy()


if __name__ == '__main__':
    main()
