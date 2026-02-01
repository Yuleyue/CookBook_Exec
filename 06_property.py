#!python3
# -*- coding: utf-8 -*-
'''
Author : "Yuleyue"
Time : 2026/2/1 11:59
Email : adamyue@163.com
'''
# class Goods():
#     @property
#     def size(self):
#         return 100
#
# if __name__ == '__main__':
#     obj = Goods()
#     ret  = obj.size
#     print(ret)

class Pager:
    def __init__(self, current_page):
        self.current_page = current_page
        self.per_items = 10

    @property
    def start(self):
        val = (self.current_page - 1) * self.per_items
        return val

    @property
    def end(self):
        val = (self.current_page * self.per_items - 1)
        return val

if __name__ == '__main__':
    p = Pager(20)
    print(f'Start form {p.start}')
    print(f'End till {p.end}')