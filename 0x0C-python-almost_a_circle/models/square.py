#!/usr/bin/python3
"""
Module containing Rectangle
Inheriting from the Rectangle class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Representation of the Square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializing the Square.
        Args:
            @size: Square's size
            @x: coordinate x
            @y: coordinate y
            @id: Square identity
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Representation of the Square size"""
        return self.width

    @size.setter
    def size(self, value):
        """Getting or setting Square's size"""
        self.width = value
        self.height = value
