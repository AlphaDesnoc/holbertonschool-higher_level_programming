#!/usr/bin/python3
"""
Module that defines a Student class.
"""


class Student:
    """
    Represents a student with a first name, last name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialize a Student instance.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieve the dictionary representation of a Student instance.
        If `attrs` is a list of attribute names,
            only those attributes are included.

        Args:
            attrs (list, optional): List of attribute names to include.

        Returns:
            dict: The dictionary representation of the student.
        """
        if attrs is None:
            return self.__dict__
        else:
            return {key: self.__dict__[key] for key
                    in attrs if key in self.__dict__}

    def reload_from_json(self, json):
        """
        Replace all attributes of the Student instance
            with values from a dictionary.

        Args:
            json (dict): Dictionary containing new attribute values.
        """
        for key in json:
            self.__dict__[key] = json[key]
