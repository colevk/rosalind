#!/usr/bin/env python3

"""
Given: A positive integer n (n≤1000).

Return: The total number of subsets of {1,2,…,n} modulo 1,000,000.

>>> main('3')
8
"""

from rosalind import *


def main(input_string):
    print(pow(2, int(input_string), 1000000))


if __name__ == '__main__':
    main(rosalind_input())
