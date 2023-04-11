#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""
Class Rectangle inheriting from BaseGeometry class
"""


class Rectangle(BaseGeometry):
    """A rectangle class inheriting basegeometry"""

    def __init__(self, width, height):
        """
        Width and height instantiation

        Args;
        @width: private instance attribute
        @height: private instance attribute
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
