#!python3
# -*- coding: utf-8 -*-
'''
Author : "Yuleyue"
Time : 2026/2/2 6:40
Email : adamyue@163.com
'''


class UpperAttrMetaClass(type):
    def __new__(cls, name, bases, attrs):
        new_attr = dict()
        for k, v in attrs.items():
            if not k.startswith('__'):
                new_attr[k.upper()] = v

        return type.__new__(cls, name, bases, new_attr)


class Foo(metaclass=UpperAttrMetaClass):
    bar = 'bip'
    bar1 = 'hello'


print(hasattr(Foo, 'bar'))
print(hasattr(Foo, 'bar1'))
print(hasattr(Foo, 'BAR'))
print(hasattr(Foo, 'BAR1'))

f = Foo()
print(f.BAR)
print(f.BAR1)
