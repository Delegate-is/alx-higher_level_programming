#!/usr/bin/python3
"""
An empty class BaseGeometry representation
"""


class BaseGeometry:
    """ empty class"""
    pass

    def area(self):
        """Area function"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Integer validation function

        Args:
        @name: parameter name
        @value: parameter value to be validated

        Raise;
        TypeError if value is not an integer
        ValueError if value is <= 0
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
