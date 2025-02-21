#!/usr/bin/python3
"""
Module that defines the Rectangle class,
which includes width and height attributes,
methods to calculate the area and perimeter,
and a string representation using '#'.
"""


class Rectangle:
    """
    Represents a rectangle defined by its width and height.

    Attributes:
        __width (int): The width of the rectangle (private).
        __height (int): The height of the rectangle (private).

    Methods:
        __init__(self, width=0, height=0): Initializes a rectangle instance.
        width(self): Gets the width of the rectangle.
        width(self, value): Sets the width of the rectangle.
        height(self): Gets the height of the rectangle.
        height(self, value): Sets the height of the rectangle.
        area(self): Calculates and returns the area of the rectangle.
        perimeter(self): Calculates and returns the perimeter of the rectangle.
        __str__(self): Returns a string representation
            of the rectangle using '#'.
        __repr__(self): Returns a string representation
            of the rectangle for reproduction.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle instance with optional width and height.

        Args:
            width (int): The width of the rectangle (default is 0).
            height (int): The height of the rectangle (default is 0).

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is negative.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle.

        Args:
            value (int): The new width value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle.

        Args:
            value (int): The new height value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculates and returns the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates and returns the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle,
                or 0 if either width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns a string representation
            of the rectangle using the '#' character.
        If the width or height is 0, returns an empty string.

        Returns:
            str: A string representation of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join("#" * self.__width for _ in range(self.__height))

    def __repr__(self):
        """
        Returns a string representation of the rectangle that allows
        the creation of a new instance using eval().

        Returns:
            str: A string representation of the rectangle
                in the format 'Rectangle(width, height)'.
        """
        return f"Rectangle({self.__width}, {self.__height})"
