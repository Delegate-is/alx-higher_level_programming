#!/usr/bin/python3
"""
Containing Square class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Representing the class square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializing Square.
        Args:
            size
            x 
            y
            id  
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
