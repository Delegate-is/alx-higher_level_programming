#!/usr/bin/python3
"""
Sub-class Square ineriting from Rectangle Class 
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square Representation"""

    def __init__(self, size):
        """
        Square class initialization
        Args:
        @size: private class attribute
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
