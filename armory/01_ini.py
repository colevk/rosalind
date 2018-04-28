#!/usr/bin/env python3

"""
Given: A DNA string s of length at most 1000 bp.

Return: Four integers (separated by spaces) representing the respective number
of times that the symbols 'A', 'C', 'G', and 'T' occur in s. Note: You must
provide your answer in the format shown in the sample output below.

>>> main('AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC')
20 12 17 21
"""

from rosalind import rosalind_input
from Bio.Seq import Seq


def main(input_string):
    s = Seq(input_string)
    print(s.count('A'), s.count('C'), s.count('G'), s.count('T'))


if __name__ == '__main__':
    main(rosalind_input())
