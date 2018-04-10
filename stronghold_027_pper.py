#!/usr/bin/env python3

"""
Given: Positive integers n and k such that 100≥n>0 and 10≥k>0.

Return: The total number of partial permutations P(n,k), modulo 1,000,000.

>>> main('21 7')
51200
"""


from rosalind import *
from scipy.special import perm


def main(input_string):
    n, r = map(int, input_string.split())
    print(perm(n, r, exact=True) % 1000000)


if __name__ == '__main__':
    main(rosalind_input())
