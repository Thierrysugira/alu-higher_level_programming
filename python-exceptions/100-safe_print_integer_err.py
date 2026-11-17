#!/usr/bin/python3
"""Defines a function that prints an integer and reports errors."""
import sys


def safe_print_integer_err(value):
    """Print an integer with "{:d}".format().

    Returns True if value was printed. Otherwise prints the error in
    stderr, preceded by "Exception: ", and returns False.
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError) as err:
        print("Exception: {}".format(err), file=sys.stderr)
        return False
