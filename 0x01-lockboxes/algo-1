#!/usr/bin/python3

'ALX interview quesntion'


def canUnlockAll(boxes):
    '''boxes is a list of lists
    A key with the same number as a box opens that box
    You can assume all keys will be positive integers
    There can be keys that do not have boxes
    The first box boxes[0] is unlocked
    Return True if all boxes can be opened, else return False
    '''
    # clone list
    boxs = boxes[:]
    for n in range(1, len(boxs)):
        for i in range(len(boxs)):
            if n in boxs[i] and 'taken' not in boxs[i]:
                # n can be unlocked
                boxs[i].append('taken')
                break
            if i == len(boxs) - 1:
                return False
    return True
