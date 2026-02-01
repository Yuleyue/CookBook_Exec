#!python3
# -*- coding: utf-8 -*-
'''
Author : "Yuleyue"
Time : 2026/2/1 10:51
Email : adamyue@163.com
'''
class MaxValDes():
    def __init__(self, init_val, max_val):
        self.value = init_val
        self.max_val = max_val
        self.data = dict()

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self.data.get(instance, self.value)

    def __set__(self, instance, value):
        self.data[instance] = min(self.max_val, value)

class Widget():
    volume = MaxValDes(0, 10)

if __name__ == '__main__':
    a = Widget()
    print('---a default volume:', a.volume)
    a.volume = 12
    print('---a after volume:', a.volume)

    b = Widget()
    print('---b default volume:', b.volume)