#!usr/bin/python3
''' ALX Interview - Lockboxes '''


def canUnlockAll(boxes):
    ''' Checks if all boxes can be unlocked '''
    keys = boxes[0]
    locked_boxes = boxes[1:]

    for n in range(1, len(boxes)):
        if n in set(keys) and boxes[n] in locked_boxes:
            keys.extend(boxes[n])
            locked_boxes.remove(boxes[n])

        for key in set(keys):
            if boxes[key] in locked_boxes:
                keys.extend(boxes[key])
                locked_boxes.remove(boxes[key])

    if locked_boxes:
        return False

    return True
