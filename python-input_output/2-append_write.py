#!/usr/bin/python3
"""Defines a function that appends a string to a text file."""


def append_write(filename="", text=""):
    """Append a string to a UTF8 text file and return the characters added.

    The file is created if it does not exist.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
