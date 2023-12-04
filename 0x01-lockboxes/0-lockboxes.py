#!/usr/bin/python3
"""
Lockboxes module
"""


def canUnlockAll(boxes):
    """
    Determine if all the boxes can be opened.

    Args:
    - boxes (list of lists): A list of lists @list is a box,
      & index of outer list is the box number.@box may contain
      keys to other boxes.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    if type(boxes) is not list or len(boxes) == 0:
        return False

    n = len(boxes)
    boxnumber = [0]

    for i in boxnumber:
        for num in boxes[i]:
            if num < n and num not in boxnumber:
                boxnumber.append(num)
    return len(boxnumber) == n
