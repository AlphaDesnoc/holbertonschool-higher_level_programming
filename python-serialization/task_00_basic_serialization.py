#!/usr/bin/python3
"""
Module providing basic serialization and deserialization functions using JSON.
"""
import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize and save data to a file in JSON format.

    Args:
        data (any): The data to be serialized.
        filename (str): The name of the file to save the serialized data.
    """
    with open(filename, 'w') as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """
    Load and deserialize data from a JSON file.

    Args:
        filename (str): The name of the file to load data from.

    Returns:
        any: The deserialized data from the file.
    """
    with open(filename, 'r') as file:
        return json.load(file)
