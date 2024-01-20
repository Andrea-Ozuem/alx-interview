#!/usr/bin/python3
'Prime Game'


def findMultiples(num, goal):
    '''
    Finds multiples of a given number within a list
    '''
    for i in goal:
        if i % num == 0:
            goal.remove(i)
    return goal


def isPrime(i):
    '''
    Check if a number is prime.
    '''
    if i == 1:
        return False
    for j in range(2, i):
        if i % j == 0:
            return False
    return True


def getPrimes(n):
    '''
    Dispatch a given set into prime numbers and non-prime numbers.
    '''
    counter = 0
    arr = list(n)
    for i in range(1, len(arr) + 1):
        if isPrime(i):
            counter += 1
            arr.remove(i)
            arr = findMultiples(i, arr)
        else:
            pass
    return counter


def isWinner(x, nums):
    '''
    Maria and Ben are playing a game. Given a set of consecutive integers
    determine who the winner of each game is.
    '''
    players = {'Maria': 0, 'Ben': 0}
    cluster = set()
    for elem in range(x):
        nums.sort()
        num = nums[elem]
        for i in range(1, num + 1):
            cluster.add(i)
            if i == num + 1:
                break
        temp = getPrimes(cluster)

        if temp % 2 == 0:
            players['Ben'] += 1
        elif temp % 2 != 0:
            players['Maria'] += 1

    if players['Maria'] > players['Ben']:
        return 'Maria'
    elif players['Maria'] < players['Ben']:
        return 'Ben'
    else:
        return None
