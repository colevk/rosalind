#!/usr/bin/env python3

"""
Given: A DNA string s of length at most 100 bp and an array A containing at
most 20 numbers between 0 and 1.

Return: An array B having the same length as A in which B[k] represents the
common logarithm of the probability that a random string constructed with the
GC-content found in A[k] will match s exactly.

>>> main('''ACGATACAA
... 0.129 0.287 0.423 0.476 0.641 0.742 0.783''')
-5.737 -5.217 -5.263 -5.360 -5.958 -6.628 -7.009
"""

from rosalind import *
from math import log10


def log10_probability(sequence, gc_content):
    """The log base 10 of the probability that a given sequence could be
    randomly generated from a pool of a given gc content."""
    probabilities = {
        'A': log10((1 - gc_content) / 2),
        'C': log10(gc_content / 2),
        'G': log10(gc_content / 2),
        'T': log10((1 - gc_content) / 2),
    }
    return sum(probabilities[c] for c in sequence)


def main(input_string):
    lines = input_string.split('\n')
    sequence = lines[0]
    gc_contents = [float(n) for n in lines[1].split()]
    probabilities = [log10_probability(sequence, gc) for gc in gc_contents]
    print(' '.join('{:.3f}'.format(p) for p in probabilities))


if __name__ == '__main__':
    main(rosalind_input())
