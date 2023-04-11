#!/usr/bin/python3
"""
inherits_from function representation
"""


def inherits_from(obj, a_class):
    """ Returns true if object is an instance of inherited class.
    Otherwise, false"""
    return (issubclass(type(obj), a_class))
