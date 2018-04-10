#!/usr/bin/env python3

"""
Given: A protein string P of length at most 1000 aa.

Return: The total weight of P. Consult the monoisotopic mass table.

>>> main('SKADYEK')
821.392
"""

from rosalind import *


def main(input_string):
    mass = sum(Protein._aa_masses[aa] for aa in input_string)
    print('{:.3f}'.format(mass))


if __name__ == '__main__':
    main(rosalind_input())
