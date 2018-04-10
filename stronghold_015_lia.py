#!/usr/bin/env python3

"""
Given: Two positive integers k (k≤7) and N (N≤2^k). In this problem, we begin
with Tom, who in the 0th generation has genotype Aa Bb. Tom has two children
in the 1st generation, each of whom has two children, and so on. Each organism
always mates with an organism having genotype Aa Bb.

Return: The probability that at least N Aa Bb organisms will belong to the
k-th generation of Tom's family tree (don't count the Aa Bb mates at each
level). Assume that Mendel's second law holds for the factors.

>>> main('2 1')
0.684
"""

from rosalind import *
from scipy.special import comb


def main(input_string):
    k, n = map(int, input_string.split())
    total = 2 ** k
    # The chance of any given descendant being Aa Bb is always 0.25
    prob = sum(
        comb(total, m) * (0.25 ** m) * (0.75 ** (total - m))
        for m in range(n, total + 1)
    )
    print('{:.3f}'.format(prob))


if __name__ == '__main__':
    main(rosalind_input())
