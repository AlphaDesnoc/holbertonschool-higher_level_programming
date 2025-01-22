#!/usr/bin/python3
def matrix_divided(matrix, div):
    """Divide all elements of a matrix by a divisor.

    Args:
        matrix (list of lists of int/float): The matrix to divide.
        div (int/float): The divisor.

    Returns:
        list of lists of float: A new matrix with each element divided
        by div, rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats,
        or if rows are not of the same size.
        TypeError: If div is not a number (integer or float).
        ZeroDivisionError: If div is zero.
    """
    if (not isinstance(matrix, list)
        or not all(isinstance(row, list)
                   for row in matrix) or
            not all(isinstance(element, (int, float))
                    for row in matrix for element in row)):
        raise TypeError("matrix must be a matrix (list of lists)" +
                        "of integers/floats")

    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(element / div, 2) for element in row] for row in matrix]
