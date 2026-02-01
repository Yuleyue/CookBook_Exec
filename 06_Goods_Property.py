#!python3
# -*- coding: utf-8 -*-
'''
Author : "Yuleyue"
Time : 2026/2/1 15:45
Email : adamyue@163.com
'''
class Goods:
    def __init__(self):
        self.original_price = 100
        self.discount_rate = 0.8

    @property
    def price(self):
        new_price = self.original_price * self.discount_rate
        return new_price

    @price.setter
    def price(self, value):
        self.original_price = value

    @price.deleter
    def price(self):
        del self.original_price

if __name__ == '__main__':
    obj = Goods()
    print(obj.price)
    obj.price = 200
    print(obj.price)
    del obj.price