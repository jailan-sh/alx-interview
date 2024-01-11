#!/usr/bin/python3
""" task 2"""


def canUnlockAll(boxes):
    """method that determines if all the boxes can be opened.
    return true if all open otherwise false
    """
    opened = set()
    n = len(boxes) - 1

    def dfs(box):
        opened.add(box)
        for k in boxes[box]:
            if k not in opened and k <= n:
                dfs(k)
    dfs(0)

    return len(boxes) == len(opened)
