#!/usr/bin/python3
"""Defining a function that prints a name"""


def say_my_name(first_name, last_name=""):
    """Printing a name.

    Args:
    @ first_name(str): the first name to be printed
    @ last_name(str): the final name to be printed
    Raise TypeError:
        If either of the argument names are not strings.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
