#!/usr/bin/python3
"""
Function writing string into a text file
"""


def write_file(filename="", text=""):
    """return number of characters after writing string into a text file"""
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)
    return len(text)
