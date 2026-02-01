#!python3
# -*- coding: utf-8 -*-
'''
Author : "Yuleyue"
Time : 2026/2/1 17:46
Email : adamyue@163.com
'''
class Game_zwdzjs():
    def __init__(self):
        self.__sun_num  = 0
    @property
    def sun_num(self):
        print('---4---')
        return self.__sun_num
    @sun_num.setter
    def sun_num(self, num):
        print('---5---')
        if num == 50:
            self.__sun_num += num
            return 'Ok'
        return 'Error'

if __name__ == '__main__':
    game = Game_zwdzjs()
    print('---0---')
    print(game.sun_num)
    print('---1---')
    game.sun_num += 50
    print('---2---')
    print(game.sun_num)
    print('---3---')
