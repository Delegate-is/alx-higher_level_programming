#!/usr/bin/python3
"""
Function returning JSON object representation
"""


import json


def to_json_string(my_obj):
    """Return JSON representation of object"""
    return (json.dumps(my_obj)
