# #!python3
# # -*- coding: utf-8 -*-
# '''
# Author : "Yuleyue"
# Time : 2026/2/1 21:48
# Email : adamyue@163.com
# '''
#
#
# class A():
#     '''An example of class'''
#     num = 10
#
#     def __init__(self):
#         pass
#
#     def func(self, value):
#         A.num += value
#         return A.num
#
#
# a = A()
# print(a.num)
# a.func(10)
# print(a.num)
#
# print('-' * 30)
#
# b = A()
# print(b.num)
# b.func(20)
#
# c = A()
# print(c.num)
#
# D = type('D', (object,), {'num': 10})
# d = D()
# print(help(d))
#
# class Adder:
#     def __init__(self,increment):
#         self.increment = increment
#     def __call__(self, number):
#         return number + self.increment
#
# if __name__ == '__main__':
#     add_five = Adder(5)
#     result = add_five(20)
#     print(result)

class A(object):
   count = 0
   def __init__(self):
       # A.count += 1
       self.__class__.count += 1
print(A.count) # 输出: 0
a = A()
print(a.count) # 输出: 1
b = A()
print(b.count) # 输出: 2
print(A.count) # 输出: 2