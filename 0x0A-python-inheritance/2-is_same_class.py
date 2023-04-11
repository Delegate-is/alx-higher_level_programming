#!/usr/bin/python3
"""
is_same_class function representation
"""

def is_same_class(obj, a_class):
    """Returns true give that object is exactly an instance in specified
    class. Otherwise, False."""
    return isinstance(obj, a_class)
