#!python3
# -*- coding: utf-8 -*-
'''
Author : "Yuleyue"
Time : 2026/2/3 22:07
Email : adamyue@163.com
'''
class_body = '''
def greeting(self):
    print("Hello World!")
def jump(self):
    print("Jump!") 
'''
class_dict = dict()
exec(class_body, globals(), class_dict)

Customer = type('Customer', (), class_dict)

c = Customer()
c.greeting()