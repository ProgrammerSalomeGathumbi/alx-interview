#!/usr/bin/python3
"""
0-lockboxes
"""


def canUnlockAll(boxes):
    """
    a method that determines if all the boxes can be opened
    Args:
        boxes (list): A list of lists representing the boxes.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    keys = [0]  # keys available from the first box
    # Loop through the available keys and open the corresponding boxes
    for key in keys:
        # Loop through the opened boxes and their keys to open more boxes
        for box in boxes[key]:
            if box not in keys and box < len(boxes):
                keys.append(box)  # add the new key to available keys
    if len(keys) == len(boxes):
        return True
    return False
