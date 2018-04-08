#!/usr/bin/env python3

"""
Given: A protein string of length at most 1000 aa.

Return: The total number of different RNA strings from which the protein could
have been translated, modulo 1,000,000. (Don't neglect the importance of the
stop codon in protein translation.)
"""

from rosalind import *
from collections import defaultdict
from functools import reduce


if __name__ == '__main__':
    number_of_encodings = defaultdict(int)
    for k, v in RNA._codons.items():
        number_of_encodings[v] += 1

    print(
        reduce(
            lambda x, y: x * y,
            [number_of_encodings[aa] for aa in rosalind_input()],
            number_of_encodings[None])
        % 1000000)
