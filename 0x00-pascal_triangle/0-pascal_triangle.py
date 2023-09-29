#!/usr/bin/python3
"""Functions to comput pascal traingle"""


def pascal_triangle(n):
    '''Pascal traingle function'''
    if n <= 0:
        return []

    res = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            row.append(combination(i, j))
        res.append(row)
    return res


def fact(n):
    ''' Takes n and return its fact'''
    return 1 if n < 2 else n * fact(n - 1)


def combination(i, j):
    ''' equivalent to iCj'''
    return fact(i) // (fact(j) * fact(i - j))
