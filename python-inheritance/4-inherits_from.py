#!/usr/bin/python3
"""
Module providing a function to check
    if an object is an instance of a subclass.
"""


def inherits_from(obj, a_class):
    """
    Check if an object is an instance of a class that inherits
    (directly or indirectly) from a specified class.

    Args:
        obj: The object to check.
        a_class: The target class.

    Returns:
        bool: True if obj is an instance of a subclass of a_class,
            otherwise False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
