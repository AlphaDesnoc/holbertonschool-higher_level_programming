#!/usr/bin/python3
"""
Module providing a function to read and
    display the contents of a text file.
"""


def read_file(filename=""):
    """
    Open a text file (UTF-8) and print its contents to the standard output.

    Args:
        filename (str): The path to the text file.
    """
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")
