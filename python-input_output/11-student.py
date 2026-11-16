#!/usr/bin/python3
"""Defines a class Student that can be saved and reloaded."""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return the dictionary representation of the Student.

        Args:
            attrs (list): Attribute names to keep. If it is not a list of
                strings, all attributes are returned.
        """
        if (isinstance(attrs, list) and
                all(isinstance(a, str) for a in attrs)):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace the attributes of the Student from a dictionary.

        Args:
            json (dict): The attribute names and their new values.
        """
        for key, value in json.items():
            setattr(self, key, value)
