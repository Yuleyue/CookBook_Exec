#!python3
# -*- coding: utf-8 -*-
'''
Author : "Yuleyue"
Time : 2026/2/3 10:26
Email : adamyue@163.com
'''

class CacheDecorator:
    def __init__(self, func):
        self.func = func
        self.cache = {}

    def __call__(self, *args, **kwargs):
        print(args)
        if args not in self.cache:
            self.cache[args] = self.func(*args, **kwargs)
        else:
            print('Fetching from cache')
        return self.cache[args]

@CacheDecorator
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))
print(factorial(6))