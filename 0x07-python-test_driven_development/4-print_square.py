#!/usr/bin/python3
"""Defining a function that prints a square"""


def print_square(size):
    """ The square is printed with the character #.
    Args:
        @ size: the length of the square.
    Raise:
    TypeError: if size is not an integer.
    ValueError: if the size of square is less than 0.
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    elif type(size) == float and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        print("#" * size)
