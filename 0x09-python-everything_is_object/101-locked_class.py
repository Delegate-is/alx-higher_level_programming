#!/usr/bin/python3
"""Defining a locked class"""


class LockedClass:
    """
    User barred from creating new instance attributes except first_name
    attribute only.
    """

    __slots__ = ["first_name"]
