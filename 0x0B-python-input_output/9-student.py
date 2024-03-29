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

    def to_json(self):
        """function retrieving dictionary representation of a
        Student instance"""
        return self.__dict__
