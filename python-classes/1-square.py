#!/usr/bin/python3
"""
This module contains the definition of a Square class
with a private size attribute.
"""


class Square:
    """
    Represents a square with a private attribute for its size.

    Attributes:
        __size (int): The length of each side of the square.
    """

    def __init__(self, size):
        """
        Constructs a Square instance with a given size.

        Args:
            size (int): The length of each side of the square.
        """
        self.__size = size
