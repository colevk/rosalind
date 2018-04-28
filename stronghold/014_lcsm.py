#!/usr/bin/env python3

"""
Given: A collection of k (k≤100) DNA strings of length at most 1 kbp each in
FASTA format.

Return: A longest common substring of the collection. (If multiple solutions
exist, you may return any single solution.)

>>> main('''>Rosalind_1
... GATTACA
... >Rosalind_2
... TAGACCA
... >Rosalind_3
... ATACA''')
TA
"""

from rosalind import *


def main(input_string):
    strings = sorted(
        (v for _, v in parse_fasta(input_string)),
        key=len
    )
    longest_substring = ''
    shortest = strings[0]
    for start in range(len(shortest)):
        for end in range(start + 1 + len(longest_substring), len(shortest) + 1):
            substring = shortest[start:end]
            for other_string in strings[1:]:
                if substring not in other_string:
                    break
            else:
                longest_substring = substring
    print(longest_substring)


if __name__ == '__main__':
    main(rosalind_input())
