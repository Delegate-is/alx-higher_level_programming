#!/usr/bin/python3
from models.base import Base
"""Inherits from Base class"""


class Rectangle:
    """Defining a rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializing the class Rectangle
        args:
            @width
            @height
            @x
            @y
        private attributes with own public setter and getter
        """
        super().__init__(id)
        self.width
        self.height
        self.x
        self.y

    @property
    def name(self):
        return self.__width

    @property
    def name(self):
        return self.__height

    @property
    def name(self):
        return self.__x

    @property
    def name(self):
        return self.__y

    @width.setter
    def name(self, value):
        self.__width = value

    @height.setter
    def name(self, value):
        self.__height = value

    @x.setter
    def name(self, value):
        self.__x = value

    @y.setter
    def name(self, value):
        self.__y = value
