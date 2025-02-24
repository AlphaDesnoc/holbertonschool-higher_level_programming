#!/usr/bin/python3
"""
This module defines a function to retrieve an object's attributes and methods.
"""


def lookup(obj):
    """
    Get a list of an object's available attributes and methods.

    Args:
        obj: The object to inspect.

    Returns:
        list: List of attributes and methods of the object.
    """
    return dir(obj)
