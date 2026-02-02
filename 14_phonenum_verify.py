#!python3
# -*- coding: utf-8 -*-
'''
Author : "Yuleyue"
Time : 2026/2/2 19:15
Email : adamyue@163.com
'''
'''
    This example demonstrates how to validate phone numbers.
    电话号码按11位格式：027-88888888，或0710-8888888，或13812345678
'''
import re

# # 电话号码 raw code
# phone_numbers = [
#     "13912345678",
#     "(010) 3456-7890",
#     "+1 (123) 456-7890"
# ]
#
# 正则表达式
patterns = [
    r'^1[3-9]\d{9}$',
    r'^\(0\d{2}\) \d{8}$',
    r'^\(0\d{3}\) \d{7}$',
    r'^\+\d{1,3} \d{1,4}(\s|\-)?\d{1,4}(\s|\-)?\d{1,4}$'
]

# 验证电话号码有效否
def validate_phone_number(phone_number):
    is_valid = any(re.match(pattern, phone_number) for pattern in patterns)
    if is_valid:
        print(f"电话号码 {phone_number} 有效。")
    else:
        print(f"电话号码 {phone_number} 无效。")
    return is_valid

class PhoneNumberType:
    '''
    Define the type of phone number to specified format
    '''
    def __init__(self, key, valid_type):
        self.key = key
        self.valid_type = valid_type
    def __get__(self, instance, owner):
        return instance.__dict__[self.key]
    def __set__(self, instance, value):
        if not validate_phone_number(value):
            raise TypeError('Invalid phone number')
        instance.__dict__[self.key] = value

def deco(**kwargs):
    def wrapper(obj):
        for key, value in kwargs.items():
            setattr(obj, key, PhoneNumberType(key, value))
        return obj
    return wrapper

@deco(phone_number=str)
class PhoneNumber:
    '''
    Define phone number class
    '''
    def __init__(self, phone_number):
        self.phone_number = phone_number
    def counter(self):
        dct = dict()
        for i in self.phone_number:
            dct[i] = dct.setdefault(i, 0) + 1
        return dct

if __name__ == '__main__':
    pn = PhoneNumber(input("Input phone number: "))
    print(pn.phone_number)
    print(pn.counter())