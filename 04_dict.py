# #!python3
# # -*- coding: utf-8 -*-
# '''
# Author : "Yuleyue"
# Time : 2026/2/1 8:20
# Email : adamyue@163.com
# '''
# class M:
#     def __init__(self):
#         self.x = 1
#
#     def __get__(self, instance, owner):
#         print('In class M, start __get__')
#         return self.x
#
#     def __set__(self, instance, value):
#         self.x = value
#
# class AA:
#     m = M()     # m is a descriptor
#     n = 2
#     def __init__(self, score):
#         self.score = score
#
# aa = AA(3)
# # print(aa.__dict__)
# # print(aa.score)
# # print(aa.__dict__['score'])
# #
# # print(type(aa).__dict__)
# # print(aa.n)
# # print(type(aa).__dict__['n'])
#
# print(aa.m)
# print(type(aa).__dict__['m'].__get__(aa, AA))
#
# print(AA.m)
# print(AA.__dict__['m'].__get__(None, AA))
#
# class A:
#     n = 2
#     def __init__(self, a):
#         self.a = a
#
# aa = A(3)
# print(aa.__dict__)
# print(type(aa).__dict__)

class M:
    def __init__(self):
        self.x = 1

    def __get__(self, instance, owner):
        print('Get m here')
        return self.x

    def __set__(self, instance, value):
        print('Set m here')
        self.x = value + 1

class N:
    def __init__(self):
        self.x = 1

    def __get__(self, instance, owner):
        print('Get n here')
        return self.x

class AA:
    m= M()
    n= N()

    def __init__(self, m, n):
        self.m = m
        self.n = n

aa = AA(2, 5)

print(aa.__dict__)
print(type(aa).__dict__)

print(aa.n)
print(AA.n)

print(aa.m)