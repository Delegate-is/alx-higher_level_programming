#!/usr/bin/python3
"""
Function returning JSON string
"""


import json


def from_json_string(my_str):
    """Return JSON representation of object(string)"""
    return (json.loads(my_str))
