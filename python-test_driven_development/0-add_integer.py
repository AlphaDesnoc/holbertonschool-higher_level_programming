#!/usr/bin/python3
def add_integer(a, b=98):
    """Add two integers or floats, casting them to integers first.

    Args:
        a (int or float): The first number.
        b (int or float): The second number, default is 98.

    Returns:
        int: The sum of a and b.

    Raises:
        TypeError: If a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)
    return a + b
