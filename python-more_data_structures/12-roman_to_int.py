#!/usr/bin/python3

def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0

    rom = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    total = 0
    prev_value = 0

    for char in reversed(roman_string):
        current_value = rom.get(char, 0)
        total += current_value if current_value >= prev_value else -current_value
        prev_value = current_value

    return total
