#!/usr/bin/env python3

"""
Given: A collection of DNA strings in FASTA format having total length at most
10 kbp.

Return: The adjacency list corresponding to O3. You may return edges in any
order.

>>> main('''>Rosalind_0498
... AAATAAA
... >Rosalind_2391
... AAATTTT
... >Rosalind_2323
... TTTTCCC
... >Rosalind_0442
... AAATCCC
... >Rosalind_5013
... GGGTGGG''')
Rosalind_0498 Rosalind_2391
Rosalind_0498 Rosalind_0442
Rosalind_2391 Rosalind_2323
"""

from rosalind import *
from collections import defaultdict
from itertools import product


def main(input_string):
    sequences = parse_fasta(input_string)
    suffixes = defaultdict(list)
    prefixes = defaultdict(list)
    for name, seq in sequences.items():
        suffixes[seq[-3:]].append(name)
        prefixes[seq[:3]].append(name)
    for key in suffixes.keys():
        for pair in product(suffixes[key], prefixes[key]):
            if pair[0] != pair[1]:
                print(pair[0], pair[1])


if __name__ == '__main__':
    main(rosalind_input())
