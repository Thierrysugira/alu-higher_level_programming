#!/usr/bin/python3
"""Defines a class BaseGeometry with an unimplemented area method."""


class BaseGeometry:
    """Represents a geometry."""

    def area(self):
        """Raise an Exception because area is not implemented."""
        raise Exception("area() is not implemented")
