#!/usr/bin/python3
"""Defining a model class Base"""


class Base:
    """Representing the base class" model
    Attrs:
        __nb_objects: instantiated base number
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializing Base class attributes.
        Args:
            @id: identity of Base(int)
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Static method returning JSON representation
        of a list of dictionaries.
        Args:
            @list_dictionaries: list of dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    def save_to_file(cls, list_objs):
        """Returning JSON string representation written to a file.
        Args:
            @list_objs: list of inherited Base class
        """
        filename = cls.__name__ + ".json"
        if list_objs is None:
            list_objs = []
        json_list = []
        for obj in list_objs:
            json_list.append(obj.to_dictionary())
        with open(filename, "w", encoding="utf-8") as file
        file.write(cls.to_json_string(json_list))

    @staticmethod
    def from_json_string(json_string):
        """Returning list representation of JSON string.
        Args:
            @json_string(string): showing list of dictionaries
        Return:
        Empty string if JSON string is None
        Otherwise, JSON string list representation
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)
