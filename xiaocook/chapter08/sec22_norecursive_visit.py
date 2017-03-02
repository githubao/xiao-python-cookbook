#!/usr/bin/env python
# encoding: utf-8

"""
@description: 不使用递归的访问者模式

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec22_norecursive_visit.py
@time: 2017/3/1 21:10
"""

import types


class Node:
    pass


class UnaryOperator(Node):
    def __init__(self, operand):
        self.operand = operand


class BinaryOperator(Node):
    def __init__(self, left, right):
        self.left = left
        self.right = right


class Add(BinaryOperator):
    pass


class Sub(BinaryOperator):
    pass


class Mul(BinaryOperator):
    pass


class Div(BinaryOperator):
    pass


class Negate(UnaryOperator):
    pass


class Number(Node):
    def __init__(self, value):
        self.value = value


class NodeVisitor:
    def visit(self, node):
        stack = [node]
        last_result = None
        while stack:
            try:
                last = stack[-1]
                if isinstance(last, types.GeneratorType):
                    stack.append(last.send(last_result))
                    last_result = None
                elif isinstance(last, Node):
                    stack.append(self._visit(stack.pop()))
                else:
                    last_result = stack.pop()
            except StopIteration:
                stack.pop()

        return last_result

    def _visit(self, node):
        method_name = 'visit_' + type(node).__name__
        meth = getattr(self, method_name, None)
        if meth is None:
            meth = self.generic_visit
        return meth(node)

    def generic_visit(self, node):
        raise RuntimeError('No {} method'.format('visit_' + type(node).__name__))


class Evaluator(NodeVisitor):
    def visit_Number(self, node):
        return node.value

    def visit_Add(self, node):
        yield (yield node.left) + (yield node.right)

    def visit_Sub(self, node):
        yield (yield node.left) - (yield node.right)

    def visit_Mul(self, node):
        yield (yield node.left) * (yield node.right)

    def visit_Div(self, node):
        yield (yield node.left) / (yield node.right)

    def visit_Negate(self, node):
        yield -(yield node.operand)


class StackCode(NodeVisitor):
    def generate_code(self, node):
        self.instructions = []
        self.visit(node)
        return self.instructions

    def visit_Number(self, node):
        self.instructions.append(('PUSH', node.value))

    def binop(self, node, instruction):
        self.visit(node.left)
        self.visit(node.right)
        self.instructions.append((instruction,))

    def visit_Add(self, node):
        self.binop(node, 'ADD')

    def visit_Sub(self, node):
        self.binop(node, 'SUB')

    def visit_Div(self, node):
        self.binop(node, 'DIV')

    def visit_Mul(self, node):
        self.binop(node, 'MUL')

    def unaryop(self, node, instruction):
        self.visit(node.operand)
        self.instructions.append((instruction,))

    def visit_Negate(self, node):
        self.unaryop(node, 'NEG')


def start_visit():
    t1 = Sub(Number(3), Number(4))
    t2 = Mul(Number(2), t1)
    t3 = Div(t2, Number(5))
    t4 = Add(Number(1), t3)

    e = Evaluator()
    print(e.visit(t4))

    s = StackCode()
    print(s.generate_code(t4))


def start_visit_no_recursive():
    a = Number(1)
    for n in range(1, 100000):
        a = Add(a, Number(1))

    e = Evaluator()
    print(e.visit(a))


def main():
    # start_visit()
    start_visit_no_recursive()


if __name__ == '__main__':
    main()
