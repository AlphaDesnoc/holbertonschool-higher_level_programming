#!/usr/bin/python3
"""Module providing functions for JSON deserialization."""

import json


def from_json_string(my_str):
    """
    Convert a JSON string representation to a Python object.

    Args:
        my_str (str): The JSON string to be deserialized.

    Returns:
        any: The Python object represented by the JSON string.
    """
    return json.loads(my_str)
