#!python3
# -*- coding: utf-8 -*-
'''
Author : "Yuleyue"
Time : 2026/2/4 12:54
Email : adamyue@163.com
'''
## stock.py

from structure import Structure
from validate import String, PositiveInteger, PositiveFloat

class Stock(Structure):
    name = String()
    shares = PositiveInteger()
    price = PositiveFloat()

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares