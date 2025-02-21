#!/usr/bin/python3
"""Defines a Square class with size validation and area calculation."""


class Square:
    """Represents a square with a private size attribute and area method."""

    def __init__(self, size=0):
        """
        Initializes a new Square instance with a validated size.

        Args:
            size (int, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            int: The area of the square (size squared).
        """
        return self.__size ** 2