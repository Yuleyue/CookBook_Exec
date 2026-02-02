#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Author: Yuleyue
Date: 2026/2/2 11:06
File: 12_descriptor.py
'''
"""
描述符：实现 __get__() __set()__ 任意两个函数
"""
class Typed:
    def __init__(self, key, valid_type):
        self.key = key
        self.valid_type = valid_type

    def __get__(self, instance, owner):
        return instance.__dict__[self.key]

    def __set__(self, instance, value):
        if not isinstance(value, self.valid_type):
            raise TypeError('Invalid data type, pls check')
        instance.__dict__[self.key] = value

def deco(**kwargs):
    def wrapper(obj):
        for key, val in kwargs.items():
            setattr(obj, key, Typed(key, val))
        return obj
    return wrapper

@deco(name=str, age=int)
class People:
    # name = Typed('name', str)
    # age = Typed('age', int)
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = People('louis', 18)
# print(p1.__dict__)  # {'name': 'louis', 'age': 18}
# p2 = People('scar', '24')  # TypeError: Invalid data type, pls check