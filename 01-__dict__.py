#!python3
# -*- coding: utf-8 -*-
'''
Author : "Yuleyue"
Time : 2026/1/31 9:34
Email : adamyue@163.com
'''
import types


class MyClass:
    '''
    THis is a class derived from object
    '''
    country = 'China'
    def __init__(self, name, count):
        self.name = name
        self.count = count
    def func(self, *args, **kwargs):
        print('func')

    @property
    def prop(self):
        print('prop')

print(MyClass.__dict__)

a = MyClass('A', 2)
print(a.__dict__)

def func_a(self):
    print('func_a')

a.ex_func = types.MethodType(func_a, a)
a.ex_func()

a.prop