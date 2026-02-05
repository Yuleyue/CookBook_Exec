#!python3
# -*- coding: utf-8 -*-
'''
Author : "Yuleyue"
Time : 2026/2/4 12:55
Email : adamyue@163.com
'''
from validate import Validator

def validate_attributes(cls):
    """
    Class decorator that extracts Validator instances
    and builds the _fields list automatically
    """
    validators = []
    for name, val in vars(cls).items():
        if isinstance(val, Validator):
            validators.append(val)

    ## Set _fields based on validator names
    cls._fields = [val.name for val in validators]

    ## Create initialization method
    cls.create_init()

    return cls

class Structure:
    _fields = ()
    _types = ()

    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError(f'Expected {len(self._fields)} arguments')
        for name, val in zip(self._fields, args):
            setattr(self, name, val)

    def __repr__(self):
        values = ', '.join(repr(getattr(self, name)) for name in self._fields)
        return f'{type(self).__name__}({values})'

    @classmethod
    def create_init(cls):
        '''
        Create an __init__ method from _fields
        '''
        body = 'def __init__(self, %s):\n' % ', '.join(cls._fields)
        for name in cls._fields:
            body += f'    self.{name} = {name}\n'

        ## Execute the function creation code
        namespace = {}
        exec(body, namespace)
        setattr(cls, '__init__', namespace['__init__'])

    @classmethod
    def __init_subclass__(cls):
        validate_attributes(cls)