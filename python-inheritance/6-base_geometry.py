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
    """

    def area(self):
        """
        Raise an exception indicating that the method is not implemented.

        Raises:
            Exception: "area() is not implemented".
        """
        raise Exception("area() is not implemented")
