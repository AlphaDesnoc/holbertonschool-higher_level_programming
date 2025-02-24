#!/usr/bin/python3
"""
Module defining a base class for geometric operations.
"""


class BaseGeometry:
    """
    Base class for geometry-related operations.

    Methods:
        area(self): Raises an exception indicating
            that the method is not implemented.
        integer_validator(self, name, value): Validates
            if a value is a positive integer.
    """

    def area(self):
        """
        Raise an exception indicating that the method is not implemented.

        Raises:
            Exception: "area() is not implemented".
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate that a parameter is a positive integer.

        Args:
            name (str): The name of the parameter.
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is not greater than 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
