#!/usr/bin/python3
"""Defines a function that checks if an object comes from a subclass."""


def inherits_from(obj, a_class):
    """Return True if obj is an instance of a subclass of a_class.

    The object must not be an instance of a_class itself.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
