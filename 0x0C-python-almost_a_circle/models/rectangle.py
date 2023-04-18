#!/usr/bin/python3
"""
Module containing Base
Rectangle class inheriting from Base class
"""
from models.base import Base


class Rectangle(Base):
    """Representation of the rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializing the class Rectangle
        Args:
            @width(int): Rectangle width
            @height(int): Rectangle height
            @x(int): x coordinate
            @y(int): y coordinate
            @id(int): Rectangle idedntity
        private attributes with own public setter and getter
        Raises:
            TypeError if input is non integer.
            ValueError if either width or height equals or is under zero.
            ValueError if either x or y is under zero.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Getting or setting Rectangle's width"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getting or setting Rectangle's height"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getting or  setting x coordinate"""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getting or setting y coordinate"""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returning the Rectangle's area."""
        return self.width * self.height

    def display(self):
        """Printing Rectangle with '#' operator."""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def __str__(self):
        """Returning a print and str representation of rectangle"""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height))
