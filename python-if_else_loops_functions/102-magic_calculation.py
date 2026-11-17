#!/usr/bin/python3
"""Defines a function rebuilt from Python bytecode."""


def magic_calculation(a, b, c):
    """Return a result depending on how a, b and c compare."""
    if a < b:
        return c
    if c > b:
        return a + b
    return a * b - c
