#!/usr/bin/python3
"""Module providing functions for JSON serialization"""

import json


def to_json_string(my_obj):
    """
    Convert an object to its JSON string representation.

    Args:
        my_obj (any): The object to be serialized.

    Returns:
        str: The JSON string representation of the object.
    """
    return json.dumps(my_obj)
