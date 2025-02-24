#!/usr/bin/python3
"""
Module providing a function to check if an
    object is an exact instance of a given class.
"""


def is_same_class(obj, a_class):
    """
    Check if an object is exactly an instance of a specified class.

    Args:
        obj: The object to check.
        a_class: The target class.

    Returns:
        bool: True if obj is an exact instance of a_class, otherwise False.
    """
    return type(obj) is a_class
