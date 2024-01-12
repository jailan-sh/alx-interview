#!/usr/bin/python3
""" task 2"""


def canUnlockAll(boxes):
    """method that determines if all the boxes can be opened.
    return true if all open otherwise false
    """
    if boxes is None:
        return False
    opened = set()
    n = len(boxes)

    def dfs(box):
        opened.add(box)
        for k in boxes[box]:
            if k < n and k not in opened:
                dfs(k)
    dfs(0)

    return len(boxes) == len(opened)

def canUnlockAll(boxes):
    """method that determines if all the boxes can be opened.
    return true if all open otherwise false
    """
    if boxes is None:
        return False
    opened = set()
    n = len(boxes)
    stack = [0]
    while stack:
        box = stack.pop()
        opened.add(box)
        for key in boxes[box]:
            if key < n and key not in opened:
                stack.append(key)
    return len(boxes) == len(opened)
