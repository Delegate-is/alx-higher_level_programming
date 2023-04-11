#!/usr/bin/python3
"""
Class Rectangle inheriting from BaseGeometry class
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A rectangle class inheriting basegeometry"""

    def __init__(self, width, height):
        """
        Rectangle class initialization
        Args;
        @width: private instance attribute
        @height: private instance attribute
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Fuction returning area of rectangle"""
        return (self.__width * self.__height)

    def __str__(self):
        """String representation of rectangle"""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))

    def __repr__(self):
        """String representation of rectangle"""
        return ("Rectangle{}/{}".format(self.__width, self.__height))
