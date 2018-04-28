#!/usr/bin/env python3

"""
Given: A positive integer n<=7.

Return: The total number of permutations of length n, followed by a list of
all such permutations (in any order).

>>> main('3')
6
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1
"""

from rosalind import *
from math import factorial
from itertools import permutations


def main(input_string):
    n = int(input_string)
    print(factorial(n))
    for p in permutations(range(1, n + 1)):
        print(' '.join(str(x) for x in p))


if __name__ == '__main__':
    main(rosalind_input())
