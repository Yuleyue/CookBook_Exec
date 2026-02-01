#!python3
# -*- coding: utf-8 -*-
'''
Author : "Yuleyue"
Time : 2026/2/1 22:50
Email : adamyue@163.com
'''
class A():
    num = 100

def print_b(self):
    print(self.num)

@staticmethod
def print_static():
    print('-----HaHa-----')
@classmethod
def print_class(cls):
    print(cls.num)

B = type('B',(A,),{'print_b':print_b, 'print_static':print_static, 'print_class':print_class})
b = B()
b.print_b()
b.print_static()
b.print_class()