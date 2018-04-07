#!/usr/bin/env python3

"""
Given: A collection of DNA strings in FASTA format having total length at most
10 kbp.

Return: The adjacency list corresponding to O3. You may return edges in any
order.
"""

from rosalind import *
from collections import defaultdict
from itertools import product


if __name__ == '__main__':
    sequences = parse_fasta(rosalind_input())
    suffixes = defaultdict(list)
    prefixes = defaultdict(list)
    for name, seq in sequences.items():
        suffixes[seq[-3:]].append(name)
        prefixes[seq[:3]].append(name)
    for key in suffixes.keys():
        for pair in product(suffixes[key], prefixes[key]):
            if pair[0] != pair[1]:
                print(pair[0], pair[1])
