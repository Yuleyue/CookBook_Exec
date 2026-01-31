#!python3
# -*- coding: utf-8 -*-
'''
Author : "Yuleyue"
Time : 2026/1/31 18:55
Email : adamyue@163.com
'''
class NameDes():
    '''
    a class to fulfil descriptor
    '''
    def __init__(self):
        self.__name = None
    def __get__(self, instance, owner):
        pass
    def __set__(self, instance, value):
        pass
    def __delete__(self, instance):
        pass

    print('---Executed In NameDes---')

class Person():
    name = NameDes()
    print('---Conducted in Person---')