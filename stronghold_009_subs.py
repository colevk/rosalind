#!/usr/bin/env python3

"""
Given: Two DNA strings s and t (each of length at most 1 kbp).

Return: All locations of t as a substring of s.

>>> main('''GATATATGCATATACTT
... ATAT''')
2 4 10
"""

import regex

from rosalind import *


def main(input_string):
    s, t = input_string.split()
    print(' '.join(str(m.start() + 1) for m in regex.finditer(t, s, overlapped=True)))


if __name__ == '__main__':
    main(rosalind_input())
