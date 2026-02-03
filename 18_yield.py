#!python3
# -*- coding: utf-8 -*-
'''
Author : "Yuleyue"
Time : 2026/2/3 20:15
Email : adamyue@163.com
'''
import time

# def squares(count:int):
#     for i in range(count):
#         yield i * i
#
# for i in squares(5):
#     print(i)
# start = time.perf_counter()
# nums = []
# for i in range(10000):
#     nums.append(i ** 2)
# stop = time.perf_counter()
# elapsed = stop - start
# print(elapsed)
class Timer:
    def __init__(self):
        self.elapsed = 0

    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, type, value, traceback):
        self.end = time.perf_counter()
        self.elapsed = self.end - self.start
        return False

with Timer() as t:
    nums = []
    for i in range(10000):
        nums.append(i ** 2)

print(t.elapsed)