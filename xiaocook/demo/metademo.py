#!/usr/bin/env python
# encoding: utf-8

"""
@description: 元类示例

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: metademo.py
@time: 2017/1/20 13:15
"""


class UpperAttrMetaClass(type):
    def __new__(cls, name, bases, attrs):
        attrs = ((key, value) for key, value in attrs.items() if not key.startswith('__'))
        upper_attrs = {key.upper(): value for key, value in attrs}
        # return type(name, bases, upper_attrs)
        # return type.__new__(cls, name, bases, upper_attrs)
        return super(UpperAttrMetaClass, cls).__new__(cls, name, bases, upper_attrs)


class Foo(metaclass=UpperAttrMetaClass):
    bar = '333'


class Foo2():
    '''
    __getattr__
    __getattribute__
    仅针对实例属性有效
    '''

    def __init__(self):
        self.bar = '333'

    # 属性不存在的时候，或者attributeError异常时，会被调用
    # 如果有 __getattribute__ 方法，那么此方法要么被显式调用，要么抛出attributeError异常时被调用

    # 如果不抛出异常或返回值，默认会返回None，而不是没有这个属性
    def __getattr__(self, item):
        # try:
        #     res = self.__getattribute__(item)
        # except:
        #     res = '444'
        # return res
        return '444'

    # 会被无条件调用
    def __getattribute__(self, item):
        return '555'


def main():
    foo2 = Foo2()

    print(foo2.bar)
    print(foo2.BAR)


def main2():
    print(hasattr(Foo, 'bar'))
    print(hasattr(Foo, 'BAR'))


# class NoInstances(type):
#     def __call__(self, *args, **kwargs):
#         raise TypeError("Can't instantite directly")
#
#
# class Spam(metaclass=NoInstances):
#     @staticmethod
#     def test(x):
#         print("Spam.test")
#
#
# def main():
#     Spam.test(2)
#     s = Spam()


if __name__ == '__main__':
    main()
