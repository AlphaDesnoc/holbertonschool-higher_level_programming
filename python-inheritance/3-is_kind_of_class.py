#!/usr/bin/python3
"""
Module providing a function to check
    if an object is an instance of a class
    or a subclass.
"""


def is_kind_of_class(obj, a_class):
    """
    Determine if an object is an instance of a given class or its subclass.

    Args:
        obj: The object to check.
        a_class: The target class.

    Returns:
        bool: True if obj is an instance of a_class or a subclass,
            otherwise False.
    """
    return isinstance(obj, a_class)
