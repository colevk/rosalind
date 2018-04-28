#!/usr/bin/env python3

"""
Say that we have strings s=s1s2⋯sm and t=t1t2⋯tn with m<n. Consider the
substring t′=t[1:m]. We have two cases:

If s=t′, then we set s<Lext because s is shorter than t (e.g., APPLE<APPLET).
Otherwise, s≠t′. We define s<Lext if s<Lext′ and define s>Lext if s>Lext′
(e.g., APPLET<LexARTS because APPL<LexARTS). Given: A permutation of at most
12 symbols defining an ordered alphabet 𝒜 and a positive integer n (n≤4).

Return: All strings of length at most n formed from 𝒜, ordered
lexicographically. (Note: As in “Enumerating k-mers Lexicographically”,
alphabet order is based on the order in which the symbols are given.)

>>> main('''D N A
... 3''')
D
DD
DDD
DDN
DDA
DN
DND
DNN
DNA
DA
DAD
DAN
DAA
N
ND
NDD
NDN
NDA
NN
NND
NNN
NNA
NA
NAD
NAN
NAA
A
AD
ADD
ADN
ADA
AN
AND
ANN
ANA
AA
AAD
AAN
AAA
"""

from rosalind import *
from itertools import product


def lexicographic_key(alphabet):
    """Return a key that, when provided to sorted(), sorts words
    lexicographically in the order provided by alphabet."""
    return lambda word: [alphabet.index(c) for c in word]


def main(input_string):
    letters, n_str = input_string.strip().split('\n')
    letters = ''.join(letters.split())
    results = []
    for n in range(1, int(n_str) + 1):
        results.extend(''.join(seq) for seq in product(letters, repeat=n))
    for seq in sorted(results, key=lexicographic_key(letters)):
        print(seq)


if __name__ == '__main__':
    main(rosalind_input())
