#!/usr/bin/python3
"""
Module containing Rectangle
Inheriting from the Rectangle class
"""
from models.base import Base
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
        Raises:
            TypeError if input is non integer.
            ValueError if either width or height equals or is under zero.
        """
        self.size = size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Representation of the Square size"""
        return self.width

    @size.setter
    def size(self, value):
        """Getting or setting Square's size"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the attributes of the Square.

        Args:
            args (tuple): The new values for the attributes, in the order:
                - id
                - size
                - x
                - y
            kwargs (dict): The new values for the attributes,
            as keyword arguments.

        Returns:
            None
        """
        attrs = ['id', 'size', 'x', 'y']
        for i, arg in enumerate(args):
            setattr(self, attrs[i], arg)
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __str__(self):
        """Returning str() and print() Square representation"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.size)

    def to_dictionary(self):
        """Returning Square dictionary representation"""
        return {
                'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y
        }
