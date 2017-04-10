#!/usr/bin/env python
# encoding: utf-8

"""
@description: 分析源码

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec24_src_code.py
@time: 2017/4/10 21:19
"""

import ast
import inspect


def execute():
    x = 42
    a = eval('2 + 3*4 + x')
    print(a)

    exec('for i in range(10):print(i)')


def parse():
    ex = ast.parse('2 + 3*4 + x', 'eval')
    print(ex)
    print(ast.dump(ex))

    top = ast.parse('for i in range(10):print(i)', 'exec')
    print(top)
    print(ast.dump(top))


class CodeAnalyzer(ast.NodeVisitor):
    def __init__(self):
        self.loaded = set()
        self.stored = set()
        self.deleted = set()

    def visit_Name(self, node):
        if isinstance(node.ctx, ast.Load):
            self.loaded.add(node.id)
        elif isinstance(node.ctx, ast.Store):
            self.stored.add(node.id)
        elif isinstance(node.ctx, ast.Del):
            self.deleted.add(node.id)


def analyze():
    code = '''
for i in range(10):
    print(i)
del i
    '''

    top = ast.parse(code, mode='exec')
    analyzer = CodeAnalyzer()
    analyzer.visit(top)
    print('Loaded: ', analyzer.loaded)
    print('Stored: ', analyzer.stored)
    print('Deleted: ', analyzer.deleted)

    exec(compile(top, '<stdin>', 'exec'))


class NameLower(ast.NodeVisitor):
    def __init__(self, lowered_names):
        self.lowered_names = lowered_names

    def visit_FunctionDef(self, node):
        code = '__globals = globals()\n'
        code += '\n'.join("{0} = __globals['{0}']".format(name) for name in self.lowered_names)
        code_ast = ast.parse(code, mode='exec')

        node.body[:0] = code_ast.body
        self.func = node


def lower_names(*namelist):
    def lower(func):
        srclines = inspect.getsource(func).splitlines()
        for n, line in enumerate(srclines):
            if '@lower_names' in line:
                break

        src = '\n'.join(srclines[n + 1:])
        if src.startswith((' ', '\t')):
            src = 'if 1:\n' + src
        top = ast.parse(src, mode='exec')

        c1 = NameLower(namelist)
        c1.visit(top)

        temp = {}
        exec(compile(top, '', 'exec'), temp, temp)

        func.__code__ = temp[func.__name__].__code__
        return func

    return lower


INCR = 1


@lower_names('INCR')
def countdown(n):
    while n > 0:
        n -= INCR


# equal
def countdown2(n):
    __globals = globals()
    INCR = __globals['INCR']
    while n > 0:
        n -= INCR


def main():
    # execute()
    # parse()
    # analyze()

    countdown(1000)


if __name__ == '__main__':
    main()
