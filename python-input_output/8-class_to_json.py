#!/usr/bin/python3
"""
Module providing a function to retrieve the dictionary
    representation of an object for JSON serialization.
"""


def class_to_json(obj):
    """
    Retrieve the dictionary description of
        an object for JSON serialization.

    Args:
        obj (any): The object to be serialized.

    Returns:
        dict: A dictionary containing simple data structures
            (list, dictionary, string, integer, and boolean).
    """
    return obj.__dict__
