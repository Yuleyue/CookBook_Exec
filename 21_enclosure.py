#!python3
# -*- coding: utf-8 -*-
'''
Author : "Yuleyue"
Time : 2026/2/4 15:59
Email : adamyue@163.com
'''


def greeting():
    message = 'Hello World!'
    value = 200

    def inner():
        print(f'{message} -> {value}')

    message = 'Secondly'

    return inner


f = greeting()

for cell in f.__closure__:
    print(cell.cell_contents)
f()
