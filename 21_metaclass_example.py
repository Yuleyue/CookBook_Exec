#!python3
# -*- coding: utf-8 -*-
'''
Author : "Yuleyue"
Time : 2026/2/4 6:16
Email : adamyue@163.com
'''
class Prop:
    def __init__(self, attr):
        self._attr = f'_{attr}'
    def get(self, obj):
        if not hasattr(obj, self._attr):
            return None
        return getattr(obj, self._attr)

    def set(self, obj, value):
        setattr(obj, self._attr, value)

class Human(type):
    @staticmethod
    def __new__(mcs, *args):
        class_ = super().__new__(mcs, *args)        # 执行到此时，student类（对象）已生成，且其中包含有props属性
        for prop_name in class_._props:                   # 根据props中的属性内容，用property()方法与setattr()方法配合，生成具体属性
            prop = Prop(prop_name)
            p_obj = property(fget=prop.get, fset=prop.set)          # property()函数将方法包装成属性
            setattr(class_, prop_name, p_obj)            # 为类设置属性
        return class_
class Student(object, metaclass=Human):
    # _props = ['name', 'age']
    _props = ('name', 'age')         # props 元组定义了 Student类的属性。这些是Student对象将拥有的属性名称。

student = Student()
print(student.name)
student.name = 'Yule'
print(student.name)

def human(cls):
    return Human(cls.__name__, cls.__bases__, dict(cls.__dict__))

@human
class Person:
    _props = ['name', 'age']

man = Person()
print(man.name)
man.name = 'Yuleyue'
print(man.name)
man.name = 'Samyue'
print(man.name)


