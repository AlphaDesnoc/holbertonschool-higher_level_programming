#!/usr/bin/python3
"""Module providing functions to write text files."""


def write_file(filename="", text=""):
    """
    Write a string to a text file (UTF-8) and
        return the number of characters written.

    Args:
        filename (str): The path to the file to write to.
        text (str): The content to be written to the file.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
