#!/usr/bin/python3
"""
Class Student
"""


class Student:
    """Student class representation"""
    def __init__(self, first_name, last_name, age):
        """function initializing Student class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """function retrieving dictionary representation of a
        Student instance"""
        if attrs is None:
            return self.__dict__
        else:
            attrs_dict = {}
            for attr in attrs:
                if hasattr(self, attr):
                    attrs_dict[attr] = getattr(self, attr)
            return attrs_dict
