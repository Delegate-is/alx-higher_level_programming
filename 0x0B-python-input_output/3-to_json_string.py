#!/usr/bin/python3
"""
Function returning JSON string
"""


import json


def to_json_string(my_obj):
    """Return JSON representation of object(string)"""
    return (json.dumps(my_obj))
