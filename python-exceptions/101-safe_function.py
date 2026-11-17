#!/usr/bin/python3
"""Defines a function that executes another function safely."""
import sys


def safe_function(fct, *args):
    """Execute fct with args and return its result.

    If anything goes wrong, print the error in stderr, preceded by
    "Exception: ", and return None.
    """
    try:
        return fct(*args)
    except Exception as err:
        print("Exception: {}".format(err), file=sys.stderr)
        return None
