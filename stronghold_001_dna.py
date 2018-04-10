#!/usr/bin/env python3

"""
Given: A DNA string s of length at most 1000 nt.

Return: Four integers (separated by spaces) counting the respective number of
times that the symbols 'A', 'C', 'G', and 'T' occur in s.

>>> main('AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC')
20 12 17 21
"""

from rosalind import *
from collections import Counter


def main(input_string):
    symbol_counts = Counter(input_string)
    print("{A} {C} {G} {T}".format(**symbol_counts))


if __name__ == '__main__':
    main(rosalind_input())
