#!/usr/bin/python3
"""Sub-class Square ineriting from Rectangle Class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square Representation"""

    def __init__(self, size):
        """Square class initialization
        Args:
            @size: private class attribute
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        return (f"[Square] {self.__size}/{self.__size}")

    def area(self):
        """Reture area of square and override Rectangle area"""


        return self.__size ** 2
