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


def main():
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
