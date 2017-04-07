# encoding: utf-8

"""
@description: 装饰器实现的类型检查

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: sec07_typecheck.py
@time: 2017/4/7 23:07
"""

from inspect import signature
from functools import wraps


def typeassert(*ty_args, **ty_kwargs):
    def decorate(func):
        if not __debug__:
            return func

        sig = signature(func)
        bound_types = sig.bind_partial(*ty_args, **ty_kwargs).arguments

        @wraps(func)
        def wrapper(*args, **kwargs):
            bound_values = sig.bind(*args, **kwargs)
            for name, value in bound_values.arguments.items():
                if name in bound_types:
                    if not isinstance(value, bound_types[name]):
                        raise TypeError('Argument {} must be {}'.format(name, bound_types[name]))
            return func(*args, **kwargs)

        return wrapper

    return decorate


@typeassert(int, z=int)
def spam(x, y, z=42):
    print(x, y, z)


def spam2(x: int, y, z: int = 42):
    print(x, y, z)


def main():
    spam(1, 2, 3)
    spam(1, '2', 3)
    spam(1, '2', '3')


if __name__ == '__main__':
    main()
