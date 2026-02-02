#!python3
# -*- coding: utf-8 -*-
'''
Author : "Yuleyue"
Time : 2026/2/2 22:20
Email : adamyue@163.com
'''
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