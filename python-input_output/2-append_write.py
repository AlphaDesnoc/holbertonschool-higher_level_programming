#!/usr/bin/python3
"""Module providing functions to append to text files."""


def append_write(filename="", text=""):
    """
    Append a string at the end of a text file (UTF-8)
        and return the number of characters added.

    Args:
        filename (str): The path to the file to append to.
        text (str): The content to be added to the file.

    Returns:
        int: The number of characters appended to the file.
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
