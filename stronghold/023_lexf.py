#!/usr/bin/env python3

"""
Given: A collection of at most 10 symbols defining an ordered alphabet, and a
positive integer n (n≤10).

Return: All strings of length n that can be formed from the alphabet, ordered
lexicographically (use the standard order of symbols in the English alphabet).

>>> main('''A C G T
... 2''')
AA
AC
AG
AT
CA
CC
CG
CT
GA
GC
GG
GT
TA
TC
TG
TT
"""

from rosalind import *
from itertools import product


def main(input_string):
    letters, n = input_string.strip().split('\n')
    letters = ''.join(letters.split())
    for seq in product(letters, repeat=int(n)):
        print(''.join(seq))


if __name__ == '__main__':
    main(rosalind_input())
