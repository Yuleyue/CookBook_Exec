#!python3
# -*- coding: utf-8 -*-
'''
Author : "Yuleyue"
Time : 2026/2/1 18:53
Email : adamyue@163.com
'''
class IntegerField:
   def __set_name__(self, owner, name):
       print(f'self: {self}, owner: {owner}, name: {name}')
       self.name = name # 自动记录属性名
   def __get__(self, instance, owner):
       # print(f'self: {self}, instance: {instance}, owner: {owner}')
       return instance.__dict__.get(self.name)
   def __set__(self, instance, value):
       # print(f'self: {self}, instance: {instance}, value: {value}')
       if not isinstance(value, int):
           raise TypeError("必须为整数！")
       instance.__dict__[self.name] = value
class User:
   age = IntegerField()
u = User()
print(vars(u))
u.age = 20 # 正确
print(vars(u))
print(u.age) # 20
# u.age = "20" # 抛出 TypeError