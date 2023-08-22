#!/usr/bin/python3
"""
0-validate_utf8
"""


def validUTF8(data):
    """
    Determine if a given data set represents a valid UTF-8 encoding.
    """
    try:
        for byte in data:
            if byte < 0 or byte > 255:
                return False

        b_data = bytes(data)
        decoded_data = b_data.decode('utf-8')
        encoded_data = decoded_data.encode('utf-8')
        return encoded_data == b_data
    except UnicodeDecodeError:
        return false
