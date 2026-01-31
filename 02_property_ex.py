#!python3
# -*- coding: utf-8 -*-
'''
Author : "Yuleyue"
Time : 2026/1/31 11:54
Email : adamyue@163.com
'''
# class Foo:
#     def get_bar(self):
#         print('-----get_bar-----Executed')
#         return 'teacher'
#
#     BAR = property(get_bar)
#
# obj = Foo()
# obj.BAR
# print(obj.BAR)
#
# B = type('B',(), {})
# print(help(B))

def upper_attr(class_name, class_parents, class_attr):
    new_attr = dict()
    for name, value in class_attr.items():
        if not name.startswith('__'):
            new_attr[name.upper()] = value

    return type(class_name, class_parents, new_attr)

class Foo(object, metaclass=upper_attr):
    bar = 'bip'

print(hasattr(Foo, 'bar'))
print(hasattr(Foo, 'BAR'))

f = Foo()
print(f.BAR)
