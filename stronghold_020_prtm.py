#!/usr/bin/env python3

"""
Given: A protein string P of length at most 1000 aa.

Return: The total weight of P. Consult the monoisotopic mass table.
"""

from rosalind import *


if __name__ == '__main__':
    mass = sum(Protein._aa_masses[aa] for aa in rosalind_input())
    print('{:.3f}'.format(mass))
