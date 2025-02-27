#!/usr/bin/python3
"""Module providing functions for JSON serialization and deserialization."""

import json


def save_to_json_file(my_obj, filename):
    """
    Write an object to a text file using its JSON representation.

    Args:
        my_obj (any): The object to be saved.
        filename (str): The name of the file where the object will be stored.
    """
    with open(filename, "w", encoding="utf-8") as myFile:
        myFile.write(json.dumps(my_obj))
