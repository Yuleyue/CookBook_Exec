#!python3
# -*- coding: utf-8 -*-
'''
Author : "Yuleyue"
Time : 2026/2/4 12:14
Email : adamyue@163.com
'''
import dataclasses

from dataclasses import dataclass, field


@dataclass
class Student:
    name: str
    age: int
    independent: bool = field()