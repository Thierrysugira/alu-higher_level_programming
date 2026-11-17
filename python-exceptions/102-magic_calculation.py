#!/usr/bin/python3
"""Defines a function rebuilt from Python bytecode."""


def magic_calculation(a, b):
    """Return a result computed from a and b, as the bytecode does."""
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception("Too far")
            else:
                result += a ** b / i
        except Exception:
            result = b + a
            break
    return result
