#!/usr/bin/python3
"""
Function that appends a string
"""


def append_write(filename="", text=""):
    """appends string at the end of a text file and return number
    of added characters"""
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(text)
    return (len(text))
