#!/usr/bin/python3
"""Defines a function that removes a character from a string."""


def remove_char_at(str, n):
    """Return a copy of the string without the character at position n.

    The position works like a C array index: a negative position or a
    position past the end returns the string unchanged.
    """
    if n < 0 or n >= len(str):
        return str[:]
    return str[:n] + str[n + 1:]
