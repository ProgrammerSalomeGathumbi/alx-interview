#!/usr/bin/python3
"""
0-validate_utf8
"""


def validUTF8(data):
    """
    Determine if a given data set represents a valid UTF-8 encoding.
    """
    b_bytes = 0

    for byte in data:
        if b_bytes == 0:
            if (byte >> 5) == 0b110 or (byte >> 5) == 0b1110:
                b_bytes = 1
            elif (byte >> 4) == 0b1110:
                b_bytes = 2
            elif (byte >> 3) == 0b11110:
                b_bytes = 3
            elif (byte >> 7) == 0b1:
                return False
        else:
            if (byte >> 6) != 0b10:
                return False
            b_bytes -= 1

    return b_bytes == 0
