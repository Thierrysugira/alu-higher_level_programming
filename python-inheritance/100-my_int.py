#!/usr/bin/python3
"""Defines a rebellious class MyInt that inherits from int."""


class MyInt(int):
    """An int whose == and != operators are inverted."""

    def __eq__(self, other):
        """Return True when the values are different (inverted ==)."""
        return int(self) != other

    def __ne__(self, other):
        """Return True when the values are equal (inverted !=)."""
        return int(self) == other

    __hash__ = int.__hash__
