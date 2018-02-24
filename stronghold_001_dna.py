#!/usr/bin/env python3

"""
Given: A DNA string s of length at most 1000 nt.

Return: Four integers (separated by spaces) counting the respective number of
times that the symbols 'A', 'C', 'G', and 'T' occur in s.
"""

from rosalind import *
from collections import Counter

if __name__ == '__main__':
    symbol_counts = Counter(rosalind_input())
    print("{A} {C} {G} {T}".format(**symbol_counts))
