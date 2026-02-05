#!python3
# -*- coding: utf-8 -*-
'''
Author : "Yuleyue"
Time : 2026/2/5 15:56
Email : adamyue@163.com
'''
import multiprocessing
import time

def task(name: str, count: int):
    print(f'{name} - start\n', end='')
    result = 0
    for i in range(count):
        result += i
    time.sleep(1)
    print(f'{name} - end with {result}')

def start_process():
    process = multiprocessing.Process(target=task, args=['A', 100])
    process.start()
    process.join()
    print(process.exitcode)

def start_process_2():
    arg_list = [('A', 100), ('B', 200), ('C', 300)]
    processes = [multiprocessing.Process(target=task, args=[name, count]) for name, count in arg_list]
    for process in processes:
        process.start()
    for process in processes:
        process.join()

if __name__ == '__main__':
    start_process_2()