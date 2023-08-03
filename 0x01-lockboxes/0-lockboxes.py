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
    n = len(boxes)  # total number of boxes
    o_boxes = set([0])  # set to store the indices of opened boxes
    keys = boxes[0]  # keys available from the first box
    # Loop through the available keys and open the corresponding boxes
    for key in keys:
        o_boxes.add(key)
        # Loop through the opened boxes and their keys to open more boxes
        for box in boxes[key]:
            if box not in o_boxes:  # check if the box is not already opened
                keys.append(box)  # add the new key to available keys
                o_boxes.add(box)  # mark the box as opened
    return len(o_boxes) == n  # Return True if all boxes are opened, else False
