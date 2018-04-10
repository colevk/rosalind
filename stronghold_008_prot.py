#!/usr/bin/env python3

"""
Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).

Return: The protein string encoded by s.

>>> main('AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA')
MAMAPRTEINSTRING
"""

from rosalind import *


def main(input_string):
    rna = RNA(input_string)
    print(rna.to_protein())


if __name__ == '__main__':
    main(rosalind_input())
