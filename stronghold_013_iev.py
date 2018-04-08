#!/usr/bin/env python3

"""
Six nonnegative integers, each of which does not exceed 20,000. The integers
correspond to the number of couples in a population possessing each genotype
pairing for a given factor. In order, the six given integers represent the
number of couples having the following genotypes:

AA-AA
AA-Aa
AA-aa
Aa-Aa
Aa-aa
aa-aa

Return: The expected number of offspring displaying the dominant phenotype in
the next generation, under the assumption that every couple has exactly two
offspring.
"""

from rosalind import *


if __name__ == '__main__':
    couples = [int(n) for n in rosalind_input().split()]
    print(
        couples[0] * 2 +
        couples[1] * 2 +
        couples[2] * 2 +
        couples[3] * 1.5 +
        couples[4] * 1 +
        couples[5] * 0
    )
