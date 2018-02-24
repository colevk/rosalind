#!/usr/bin/env python3

"""
Given: A DNA string s of length at most 1000 bp.

Return: The reverse complement sc of s.
"""

from rosalind import *

if __name__ == '__main__':
    dna = DNA(rosalind_input())
    print(dna.reverse_complement())
