#!/usr/bin/python3
"""Defines a class Square that can be compared by area."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int or float): The size of the square.
        """
        self.size = size

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square."""
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return self.__size ** 2

    def __eq__(self, other):
        """Check if the area of two squares is equal."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Check if the area of two squares is different."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Check if the area is less than the other's area."""
        return self.area() < other.area()

    def __le__(self, other):
        """Check if the area is less than or equal to the other's."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Check if the area is greater than the other's area."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Check if the area is greater than or equal to the other's."""
        return self.area() >= other.area()
