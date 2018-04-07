#!/usr/bin/env python3

"""
Given: Two DNA strings s and t (each of length at most 1 kbp).

Return: All locations of t as a substring of s.
"""

import re

from rosalind import *

if __name__ == '__main__':
    s, t = rosalind_input().split()
    print(' '.join(str(m.start() + 1) for m in re.finditer('(?={})'.format(t), s)))
