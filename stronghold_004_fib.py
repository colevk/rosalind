#!/usr/bin/env python3

'''
Given: Positive integers n≤40 and k≤5.

Return: The total number of rabbit pairs that will be present after n months,
if we begin with 1 pair and in each generation, every pair of reproduction-age
rabbits produces a litter of k rabbit pairs (instead of only 1 pair).
'''

from rosalind import *

def fib(n, k):
    '''A modified fibonacci sequence, where F_n = F_n-1 + k * F_n-2.'''
    if n <= 2:
        return 1
    return fib(n - 1, k) + k * fib(n - 2, k)


if __name__ == '__main__':
    n, k = [int(x) for x in rosalind_input().split()]
    print(fib(n, k))
