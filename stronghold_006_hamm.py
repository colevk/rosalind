#!/usr/bin/env python3

"""
Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).

Return: The Hamming distance d_H(s,t).
"""

from rosalind import *

if __name__ == '__main__':
    string_a, string_b = map(DNA, rosalind_input().split('\n'))
    print(string_a.hamming_distance(string_b))
