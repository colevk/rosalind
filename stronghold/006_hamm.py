#!/usr/bin/env python3

"""
Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).

Return: The Hamming distance d_H(s,t).

>>> main('''GAGCCTACTAACGGGAT
... CATCGTAATGACGGCCT''')
7
"""

from rosalind import *


def main(input_string):
    string_a, string_b = map(DNA, input_string.split('\n'))
    print(string_a.hamming_distance(string_b))


if __name__ == '__main__':
    main(rosalind_input())
