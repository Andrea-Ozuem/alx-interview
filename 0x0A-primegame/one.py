#!/usr/bin/python3
'Prime Game'


def isWinner(x, nums):
    '''Prime Game Algorithm
    :nums is an array of n
    You can assume n and x will not be larger than 10000
    Return: name of the player that won the most rounds
    '''
    if x != len(nums):
        return None
    ben = maria = 1

    # flag indicates turn: 0 - M; 1 - B
    for n in nums:
        current = set(range(1, n + 1))
        flag = 0
        while True:
            primes = getPrimeList(current)
            if not primes:
                break
            multiples = getMultiples(list(primes)[0], current)
            current = current - multiples
            if flag == 0:
                flag = 1
            else:
                flag = 0
        if flag == 0:
            maria -= 1
        else:
            ben -= 1

    if ben > maria:
        return 'Ben'
    elif maria > ben:
        return 'Maria'
    else:
        return None


def getMultiples(n, arr):
    '''Gets all multiples of n in arr'''
    multiples = set()
    for i in arr:
        if i % n == 0:
            multiples.add(i)
    return multiples


def getPrimeList(arr):
    '''Gets all prime numbers between 1 and n'''
    primes = set()
    flag = 0
    for i in arr:
        # Skip 1 as1 is neither prime nor composite
        if (i == 1):
            continue
        # flag variable to tell
        # if i is prime or not
        flag = 1
        for j in range(2, i // 2 + 1):
            if (i % j == 0):
                flag = 0
                break

        # flag = 1 means i is prime
        # and flag = 0 means i is not prime
        if (flag == 1):
            primes.add(i)
    return primes
