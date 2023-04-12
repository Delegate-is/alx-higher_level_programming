#!/usr/bin/python3
"""
Function returning JSON string
"""


import json


def save_to_json_file(my_obj, filename):
    """writes an Object using JSON to a text file"""
    with open(filename, 'w', encoding='utf-8')as file:
        return json.dump(my_obj, file)
