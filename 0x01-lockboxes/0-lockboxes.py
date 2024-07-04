#!/usr/bin/python3
"""Determine if boxes can be opened"""


def canUnlockAll(boxes):
    opened = set()
    opened.add(0)
    for i in range(len(boxes)):
        if i not in opened:
            return False
        for key in boxes[i]:
            opened.add(key)
    return True

