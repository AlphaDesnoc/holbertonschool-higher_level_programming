#!/usr/bin/python3
"""
Module defining a Rectangle class that inherits from BaseGeometry.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Represents a rectangle, inheriting from BaseGeometry.

    Methods:
        __init__(self, width, height): Initializes the rectangle
            with width and height.
        area(self): Returns the area of the rectangle.
        __str__(self): Returns a string representation of the rectangle.
    """

    def __init__(self, width, height):
        """
        Initialize a rectangle with width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is not greater than 0.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculate and return the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Return a string representation of the rectangle.

        Returns:
            str: A string in the format "[Rectangle] width/height".
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
