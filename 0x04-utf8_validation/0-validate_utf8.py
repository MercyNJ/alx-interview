#!/usr/bin/python3
"""
Module contains a function to determine if a given data set
represents a valid UTF-8 encoding.
A character in UTF-8 can be 1 to 4 bytes long.
The data set can contain multiple characters.
The data will be represented by a list of integers.
Each integer represents 1 byte of data, therefore only the
8 least significant bits of each integer need to be handled.
"""


def validUTF8(data):
    """
    Check if the given list of integers represents a valid UTF-8 encoding.

    Parameters:
    - data (list): List of integers representing 1 byte of data each.

    Returns:
    - bool: True if data is a valid UTF-8 encoding, else False.
    """

    num_of_bytes = 0

    for value in data:
        value = value & 0xFF

        if num_of_bytes > 0:
            if (value >> 6) != 0b10:
                return False
            num_of_bytes -= 1

        else:
            if (value >> 7) == 0:
                num_of_bytes = 0
            elif (value >> 5) == 0b110:
                num_of_bytes = 1
            elif (value >> 4) == 0b1110:
                num_of_bytes = 2
            elif (value >> 3) == 0b11110:
                num_of_bytes = 3
            else:
                return False
    return num_of_bytes == 0
