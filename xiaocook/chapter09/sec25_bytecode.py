#!/usr/bin/env python
# encoding: utf-8

"""
@description: 字节码

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec25_bytecode.py
@time: 2017/4/10 21:48
"""

import dis
import opcode
import types


def countdown(n):
    while n > 0:
        print('T-minus: ', n)
        n -= 1
    print('Complete!')


def run():
    res = dis.dis(countdown)
    print(res)

    c = countdown.__code__.co_code
    a = opcode.opname[c[0]]
    print(opcode.opname[c[0]])
    print(opcode.opname[c[3]])


def generate_opcodes(codebytes):
    extended_arg = 0
    i = 0
    n = len(codebytes)
    while i < n:
        op = codebytes[i]
        i += 1
        if op > opcode.HAVE_ARGUMENT:
            oparg = codebytes[i] + codebytes[i + 1] * 256 + extended_arg
            extended_arg = 0
            i += 2
            if op == opcode.EXTENDED_ARG:
                extended_arg = oparg * 65536
                continue
        else:
            oparg = None
            yield (op, oparg)


def gen():
    for op, oparg in generate_opcodes(countdown.__code__.co_code):
        print(op, opcode.opname[op], oparg)


def add(x, y):
    return x + y


def broken():
    magic()
    add(2, 3)

def magic():
    c = add.__code__
    print(c.co_code)
    newbytecode = b'xxxxxxx'
    nc = types.CodeType(c.co_argcount, c.co_kwonlyargcount, c.co_nlocals, c.co_stacksize, c.co_flags, newbytecode,
                        c.co_consts, c.co_names, c.co_varnames, c.co_filename, c.co_name, c.co_firstlineno, c.co_lnotab)

    print(nc)
    add.__code__ = nc


def main():
    # run()
    # gen()
    broken()


if __name__ == '__main__':
    main()
