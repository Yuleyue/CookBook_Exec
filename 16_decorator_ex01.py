#!python3
# -*- coding: utf-8 -*-
'''
Author : "Yuleyue"
Time : 2026/2/3 9:44
Email : adamyue@163.com
'''
def log(msg):
   def decorator(func):
       def wrapper(*args, **kwargs):
           print(f"[{msg}] 开始执行 {func.__name__}")        # 测试开始执行hello
           result = func(*args, **kwargs)                   # Hello Python
           print(f"[{msg}] 结束执行 {func.__name__}")        # 测试结束执行hello
           return result
       return wrapper
   return decorator
@log("测试")
def hello(name):
   print(f"Hello, {name}")
hello("Python")