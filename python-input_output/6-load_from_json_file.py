#!/usr/bin/python3
"""Module providing functions for JSON serialization and deserialization."""

import json


def load_from_json_file(filename):
    """
    Create an object from a JSON file.

    Args:
        filename (str): The name of the file to read from.

    Returns:
        any: The Python object loaded from the JSON file.
    """
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
