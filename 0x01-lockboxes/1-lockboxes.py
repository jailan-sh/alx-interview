#!/usr/bin/python3
""" task 2"""


def canUnlockAll(boxes):
    """method that determines if all the boxes can be opened.
    return true if all open otherwise false
    """
    if boxes is None:
        return False
    opened = set()
    n = len(boxes) - 1

    def dfs(box):
        opened.add(box)
        for k in boxes[box]:
            if k <= n and k not in opened and k > 0:
                dfs(k)
    dfs(0)

    return len(boxes) == len(opened)

def canUnlockAll(boxes):
    """method that determines if all the boxes can be opened.
    return true if all open otherwise false
    """
    num_boxes = len(boxes)
    unlocked = [False] * num_boxes
    unlocked[0] = True
    queue = [0]  

    while queue:
        current_box = queue.pop(0)
        for key in boxes[current_box]:
            if 0 <= key < num_boxes and not unlocked[key]:
                unlocked[key] = True
                queue.append(key)

    return all(unlocked)
