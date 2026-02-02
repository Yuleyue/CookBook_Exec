#!python3
# -*- coding: utf-8 -*-
'''
Author : "Yuleyue"
Time : 2026/2/2 18:58
Email : adamyue@163.com
'''


def validate_email(email):
    import re
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        raise ValueError(f"Invalid email format: {email}")


def non_negative(value):
    if value < 0:
        raise ValueError("Value cannot be negative")
    return value


class Person:
    def __init__(self, name, age, email):
        self.name = name
        self._age = age
        self._email = email

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = non_negative(value)

    @property  # @property 装饰器使得我们可以将类的方法当作属性一样被访问。
    def email(self):
        return self._email

    @email.setter  # @<propertyname>.setter 装饰器允许我们定义设置属性值时的行为，比如进行验证或修改存储的值。
    def email(self, value):
        validate_email(value)
        self._email = value


# 使用示例
p = Person("Alice", 30, "alice@example.com")
print(p.age)  # 30
print(p.email)  # alice@example.com

p.age = -1  # 将引发 ValueError
p.email = "not-an-email"  # 将引发 ValueError

