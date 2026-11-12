#!/usr/bin/python3
"""Defines a function that adds a new attribute to an object."""


def add_attribute(obj, name, value):
    """Add a new attribute to an object if it is possible.

    Args:
        obj: The object to change.
        name (str): The name of the new attribute.
        value: The value of the new attribute.

    Raises:
        TypeError: If the object cannot have new attributes.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
