#!/usr/bin/python3
"""Defines a function that inserts text after lines with a given string."""


def append_after(filename="", search_string="", new_string=""):
    """Insert a line of text after each line containing a string.

    Args:
        filename (str): The name of the UTF8 text file to update.
        search_string (str): The string to look for in each line.
        new_string (str): The text to insert after every matching line.
    """
    with open(filename, encoding="utf-8") as f:
        lines = f.readlines()
    with open(filename, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
