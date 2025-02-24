#!/usr/bin/python3
"""
Module defining a Square class that inherits from Rectangle.
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Represents a square, inheriting from Rectangle.

    Methods:
        __init__(self, size): Initializes the square with the given size.
        area(self): Returns the area of the square.
        __str__(self): Returns a string representation of the square.
    """

    def __init__(self, size):
        """
        Initialize the square with the given size.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than or equal to 0.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def __str__(self):
        """
        Return a string representation of the square.

        Returns:
            str: A string in the format "[Square] size/size".
        """
        return f"[Square] {self.__size}/{self.__size}"
