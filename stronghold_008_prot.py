#!/usr/bin/env python3

"""
Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).

Return: The protein string encoded by s.
"""

from rosalind import *

if __name__ == '__main__':
    rna = RNA(rosalind_input())
    print(rna.to_protein())
