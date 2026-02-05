#!python3
# -*- coding: utf-8 -*-
'''
Author : "Yuleyue"
Time : 2026/2/3 22:23
Email : adamyue@163.com
'''
# class Human(type):
#     @staticmethod
#     def __new__(mcs, *args, **kwargs):
#         class_ = super().__new__(mcs, *args)
#         if kwargs:
#             for key, value in kwargs.items():
#                 setattr(class_, key, value)
#         return class_
#
# class Person(metaclass=Human, country='China', freedom=True):
#     pass
#
# print(Person.freedom)
# print(Person.country)

# Example 2:
import operator

class StructTupleMeta(type):
    def __init__(cls, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for n, name in enumerate(cls._fields):
            setattr(cls, name, property(operator.itemgetter(n)))

class StructTuple(tuple, metaclass=StructTupleMeta):
    _fields = list()
    def __new__(cls, *args):
        if len(args) != len(cls._fields):
            raise ValueError('{} arguments required'.format(len(cls._fields)))
        return super().__new__(cls, args)

class Stock(StructTuple):
    _fields = ['name', 'shares', 'price']

class Point(StructTuple):
    _fields = ['x', 'y']

s = Stock('ACME', 50, 91.1)
print(s)
print(s.name)

# # Example 3:
# import operator
#
# class StructTupleMeta(type):
#     @staticmethod
#     def __new__(mcs, *args):
#         class_ = super().__new__(mcs, *args)
#         for n, name in enumerate(class_._fields):
#             setattr(class_, name, property(operator.itemgetter(n)))
#         return class_
#
# class StructTuple(tuple, metaclass=StructTupleMeta):
#     _fields = list()
#
# class Stock(StructTuple):
#     _fields = ['name', 'shares', 'price']
#
# class Point(StructTuple):
#     _fields = ['x', 'y']
#
# s = Stock(('ACME', 50, 91.1))
# print(s)
# print(s.name)
# print(s.shares)
