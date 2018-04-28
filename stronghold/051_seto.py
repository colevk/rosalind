#!/usr/bin/env python3

"""
Given: A positive integer n (n≤20,000) and two subsets A and B of {1,2,…,n}.

Return: Six sets: A∪B, A∩B, A−B, B−A, Ac, and Bc (where set complements are
taken with respect to {1,2,…,n}).
>>> main('''10
... {1, 2, 3, 4, 5}
... {2, 8, 5, 10}''')
{1, 2, 3, 4, 5, 8, 10}
{2, 5}
{1, 3, 4}
{8, 10}
{6, 7, 8, 9, 10}
{1, 3, 4, 6, 7, 9}
"""

from rosalind import *
from ast import literal_eval


def main(input_string):
    lines = input_string.split('\n')
    n = int(lines[0])
    set_a = literal_eval(lines[1])
    set_b = literal_eval(lines[2])
    universe = set(range(1, n + 1))
    print(set_a | set_b)
    print(set_a & set_b)
    print(set_a - set_b)
    print(set_b - set_a)
    print(universe - set_a)
    print(universe - set_b)


if __name__ == '__main__':
    main(rosalind_input())
