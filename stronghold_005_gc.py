#!/usr/bin/env python3

"""
Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

Return: The ID of the string having the highest GC-content, followed by the
GC-content of that string. Rosalind allows for a default error of 0.001 in all
decimal answers unless otherwise stated; please see the note on absolute error
below.
"""

from rosalind import *

if __name__ == '__main__':
    dataset = parse_fasta(rosalind_input())
    key = max(dataset, key=lambda x: dataset[x].gc_count())
    print(key)
    print(dataset[key].gc_count() * 100)
