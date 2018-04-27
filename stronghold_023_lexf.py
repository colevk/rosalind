#!/usr/bin/env python3

"""
Assume that an alphabet 𝒜 has a predetermined order; that is, we write the
alphabet as a permutation 𝒜=(a1,a2,…,ak), where a1<a2<⋯<ak. For instance, the
English alphabet is organized as (A,B,…,Z).

Given two strings s and t having the same length n, we say that s precedes t
in the lexicographic order (and write s<Lext) if the first symbol s[j] that
doesn't match t[j] satisfies sj<tj in 𝒜.

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
