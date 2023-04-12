#!/usr/bin/python3
"""
Function returning JSON string
"""


import json


def load_from_json_file(filename):
    """creates an Object file using JSON file"""
    with open(filename, encoding='utf-8')as file:
        return json.load(file)
