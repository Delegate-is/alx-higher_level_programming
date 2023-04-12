#!/usr/bin/python3
"""
Function returning JSON string
"""


def class_to_json(obj):
    """Return dictionary description of an object using JSON serialization
    with simplae data structure(boolean, list, dictionary, string and
    integer)"""
    return obj.__dict__
