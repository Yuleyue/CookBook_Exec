#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Author: Yuleyue
Date: 2026/2/2 11:06
File: 12_descriptor.py
'''
"""
方法一：单纯通过描述符方式
class Typed:
    def __init__(self, expected_type):
        self.expected_type = expected_type

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError(f"Expected {self.expected_type}, got {type(value)}")
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name

class Person:
    age = Typed(int)
    name = Typed(str)

p = Person()
p.age = 25  # 正常赋值
try:
    p.age = "twenty-five"  # 会抛出 TypeError 异常
except TypeError as e:
    print(e)
    
方法二：    
通过描述符以及装饰器来实现对用户数据进行类型校验；
装饰器定义好类的属性类型，实例化时会在装饰器中校验People的name类型以及age类型
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
    def wrapper(cls):
        for key, val in kwargs.items():
            setattr(cls, key, Typed(key, val))    # 为cls类(People)增加了name = Typed('name', str), age = Typed('age', int) 两个类属性
        return cls
    return wrapper

# 类在定义时就被装饰器处理了，并没有实例化再处理，这是因为装饰器在Python中是在定义时即可执行的，不需要等到类的实例被创建
# 通过deco装饰器，类People在定义时就被动态地添加了新的类属性：name = Typed('name', str), age = Typed('age', int)共两个类实例
@deco(name=str, age=int)            # **kwargs: {'name':str, 'age':int}
class People:                       # equal to: People_obj = deco(name=str, age=int)(People)
    # name = Typed('name', str)
    # age = Typed('age', int)
    def __init__(self, name, age):
        self.name = name            # 描述符对象name，启用其__set__方法
        self.age = age              # 描述符对象age，启用其__set__方法

p1 = People('louis', 18)
print(p1.__dict__)  # {'name': 'louis', 'age': 18}
p2 = People('scar', '24')  # TypeError: Invalid data type, pls check