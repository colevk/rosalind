#!/usr/bin/env python3

"""
Given: A DNA string s of length at most 1000 bp.

Return: The reverse complement sc of s.

>>> main('AAAACCCGGT')
ACCGGGTTTT
"""

from rosalind import *


def main(input_string):
    dna = DNA(input_string)
    print(dna.reverse_complement())


if __name__ == '__main__':
    main(rosalind_input())
