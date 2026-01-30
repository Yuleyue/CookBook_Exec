#!python3
# -*- coding: utf-8 -*-
'''
Author : "Yuleyue"
Time : 2026/1/30 22:22
Email : adamyue@163.com
'''

def demo_func(func):
    def wrapper(*args, **kwargs):
        print('Before func')
        ret = func(*args, **kwargs)
        print(ret)
        print('After func')
        return ret
    return wrapper

@demo_func
def add(a, b):
    return a + b

if __name__ == '__main__':
    add(1, 2)
