#!/usr/bin/python3
""" class Rectangle defining a rectangle """


class Rectangle:
    """ Representation of an empty class Rectangle
    Public class attribute number_of_instances: """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """ Initialization of a new rectangle.
        Args:
        @width(int): The rectangle's width
        @height(int): The rectangle's height
        """

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        """ Returning a string printable presentation of the rectangle.
        Using the #character to represent the rectangle"""
        if self.width == 0 or self.height == 0:
            return ""

        """Initialize an empty string representation of the rectangle"""
        rect = ""
        for i in range(self.height):
            row_str = "#" * self.__width
            rect += row_str
            if i != self.__height - 1:
                rect += "\n"
        return rect

    def __repr__(self):
        """Return string representation of rectangle.
        Also able to create new instance applying eval()"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """ Return message when instance of the rectangle is deleted"""
        print("Bye rectangle...")
