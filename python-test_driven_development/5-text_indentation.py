#!/usr/bin/python3
def text_indentation(text):
    """Prints a text with 2 new lines after each '.', '?', or ':'.

    Args:
        text (str): The text to be formatted.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""
    skip_space = True

    for char in text:
        if char in ".?:":
            result += char + "\n\n"
            skip_space = True
        elif char == " " and skip_space:
            continue
        else:
            result += char
            skip_space = False

    print(result.strip())
