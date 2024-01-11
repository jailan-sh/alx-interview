#!/usr/bin/python3
""" task 2"""


def canUnlockAll(boxes):
    """method that determines if all the boxes can be opened.
    return true if all open otherwise false
    """
    opened = set()
    n = len(boxes) - 1
    if n == 1:
        return True

    def dfs(box):
        opened.add(box)
        for k in boxes[box]:
            if k <= n and k not in opened and k > 0:
                dfs(k)
    dfs(0)

    return len(boxes) == len(opened)
