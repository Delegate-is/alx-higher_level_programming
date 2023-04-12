#!/usr/bin/python3
"""
Function that reads a text file
"""


def read_file(filename=""):
    """prints text file to stdout after reading it (UTF8)"""
    with open(filename, mode='r', encoding='utf-8') as a file:
        for line in file:
            print(line, end="")
