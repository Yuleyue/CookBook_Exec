#!python3
# -*- coding: utf-8 -*-
'''
Author : "Yuleyue"
Time : 2026/2/1 18:28
Email : adamyue@163.com
'''
class Money():
    def __init__(self):
        self.__money = 0
    @property
    def money(self):
        return self.__money
    @money.setter
    def money(self, value):
        if isinstance(value, int):
            self.__money = value
        else:
            print('Error: not an int value')

if __name__ == '__main__':
    a = Money()
    a.money = 100
    print(a.money)
    a.money = 'hello'
    print(a.money)

