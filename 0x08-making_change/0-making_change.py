#!/usr/bin/python3
'Making change algorithm'
import math


def makeChange(coins, total):
    '''Return: fewest number of coins needed to meet total'''
    if total <= 0:
        return 0
    count = 0
    coins.sort(reverse=True)
    for i in coins:
        if total <= 0:
            break
        if total / i < 1:
            continue
        count += total // i
        total = total % i
    if total == 0:
        return count
    return -1
