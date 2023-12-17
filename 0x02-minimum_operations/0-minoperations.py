#!/usr/bin/python3
'''
    Minimum Operations
'''


def minOperations(n):
    '''
        Calculate fewest number of operations required
        to paste n operations.
    '''
    total = 0
    d = 2

    while n > 1:
        while not n % d:
            total += d
            n /= d
        d += 1

    return total
