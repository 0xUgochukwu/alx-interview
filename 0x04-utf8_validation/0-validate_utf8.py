#!/usr/bin/python3
'''
    ALX Interview - UTF-8 Validation.
'''


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data (List[int]): List of integers representing the UTF-8 data.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """
    num_bytes_to_follow = 0

    for byte in data:
        byte_bin = format(byte, '08b')

        if num_bytes_to_follow == 0:
            if byte_bin.startswith('0'):
                continue
            elif byte_bin.startswith('110'):
                num_bytes_to_follow = 1
            elif byte_bin.startswith('1110'):
                num_bytes_to_follow = 2
            elif byte_bin.startswith('11110'):
                num_bytes_to_follow = 3
            else:
                return False
        else:
            if not byte_bin.startswith('10'):
                return False
            num_bytes_to_follow -= 1

    return num_bytes_to_follow == 0
