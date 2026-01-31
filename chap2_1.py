#!python3
# -*- coding: utf-8 -*-
'''
Author : "Yuleyue"
Time : 2026/1/30 22:22
Email : adamyue@163.com
'''

# class Parent():
#     def __init__(self, name,  *args, **kwargs): # to avoid error, use args
#         print('parent init start')
#         self.name = name
#         print('parent init stop')
#
# class Child1(Parent):
#     def __init__(self, name, age, *args, **kwargs):
#         print('child1 init start')
#         self.age = age
#         super().__init__(self, *args, **kwargs)
#         print('child1 init stop')
#
# class Child2(Parent):
#     def __init__(self, name, gender, *args, **kwargs):
#         print('child2 init start')
#         self.gender = gender
#         super().__init__(self, *args, **kwargs)
#         print('child2 init stop')
#
# class GrandChild(Child1, Child2):
#     def __init__(self, name, age, gender, *args, **kwargs):
#         print('grandchild init start')
#         super().__init__(name, age, gender)
#
# print(GrandChild.__mro__)
#
# grandson = GrandChild('Tom', 18, 'male')
# print(grandson.name)

class A():
    num = 100
    func = lambda self, x : x * x

a = A()
print(a.num)
print(a.func)
print(a.func(a.num))