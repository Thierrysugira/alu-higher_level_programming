#!/usr/bin/python3
"""Defines a class LockedClass that restricts new instance attributes."""


class LockedClass:
    """Prevents creating instance attributes other than first_name."""

    __slots__ = ["first_name"]

    def __setattr__(self, name, value):
        """Only allow the attribute first_name to be set."""
        if name != "first_name":
            raise AttributeError(
                "'LockedClass' object has no attribute '{}'".format(name))
        super().__setattr__(name, value)
