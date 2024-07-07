#!/usr/bin/python3
"""Solve the unlock boxes task"""


def canUnlockAll(boxes):
    """Determines if boxes can unlock
    Args:
        boxes: List of all boxes
    Returns: True if can be opened or False if otherwise
    """
    opened = set()
    opened.add(0)
    for i in range(len(boxes)):
        if i not in opened and boxes[i]:
            return False
        for key in boxes[i]:
            opened.add(key)
    return True
