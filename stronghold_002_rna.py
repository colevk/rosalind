#!/usr/bin/env python3

"""
Given: A DNA string t having length at most 1000 nt.

Return: The transcribed RNA string of t.

>>> main('GATGGAACTTGACTACGTAAATT')
GAUGGAACUUGACUACGUAAAUU
"""

from rosalind import *


def main(input_string):
    dna = DNA(input_string)
    print(dna.to_rna())


if __name__ == '__main__':
    main(rosalind_input())
