#!/usr/bin/python3
""" class Rectangle defining a rectangle """


class Rectangle:
    """ Representation of an empty class Rectangle """

    def __init__(self, width=0, height=0):
        """ Initialization of a new rectangle.
        Args:
        @width(int): The rectangle's width
        @height(int): The rectangle's height
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """ Retrieve the rectangle's width/ setting the rectangle's width """
        return self.__width

    @width.setter
    def width(self, value):
        """ A private instance width attribute """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Getting the rectangle's height/ setting the rectangle's height """
        return self.__height

    @height.setter
    def height(self, value):
        """ A private instance height attribute """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Area of the rectangle"""
        return (self.width * self.height)

    def perimeter(self):
        """ Perimeter of the rectangle"""
        if self.width == 0 or self.height == 0:
            p = 0
        else:
            p = ((2 * self.width) + (2 * self.height))
        return p
