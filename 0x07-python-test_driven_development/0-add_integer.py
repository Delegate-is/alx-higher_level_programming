#!/usr/bin/python3
"""Defining a function that adds two integers or floats"""

def add_integer(a, b=98):
    """ Adding two integers or floats and return result.
    Parameters:
        @a: First number to add either integer or float
        @b: Second number to add either integer or float
    
    Function casts floats into integers before executing.
    
    TypeError is raised if either of the arguments is non-float or non-integer.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
