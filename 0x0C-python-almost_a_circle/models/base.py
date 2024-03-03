#!/usr/bin/python3
"""Defines the Base class."""

import json

class Base:
    """Represents the base class."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes a new Base instance."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

