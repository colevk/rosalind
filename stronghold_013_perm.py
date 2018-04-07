#!/usr/bin/env python3


"""
Given: A positive integer n≤7.

Return: The total number of permutations of length n, followed by a list of
all such permutations (in any order).
"""


from rosalind import *
from math import factorial
from itertools import permutations


if __name__ == '__main__':
    n = int(rosalind_input())
    print(factorial(n))
    for p in permutations(range(1, n + 1)):
        print(' '.join(str(x) for x in p))
