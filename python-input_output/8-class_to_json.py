#!/usr/bin/python3
"""Defines a function that returns the dictionary of an object."""


def class_to_json(obj):
    """Return the dictionary description of an object for JSON serialization.

    Args:
        obj: An instance of a class whose attributes are serializable.
    """
    return obj.__dict__
