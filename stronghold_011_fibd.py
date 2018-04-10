#!/usr/bin/env python3

"""
Given: Positive integers n<=100 and m<=20.

Return: The total number of pairs of rabbits that will remain after the n-th
month if all rabbits live for m months.

>>> main('6 3')
4
"""

from rosalind import *


@memoize
def fib_with_mortality(n, m):
    if n < 1:
        return 0
    if n == 1:
        return 1
    return fib_with_mortality(n - 1, m) + _fib_births(n, m) - _fib_deaths(n, m)

@memoize
def _fib_births(n, m):
    if n < 1:
        return 0
    if n == 1:
        return 1
    return fib_with_mortality(n - 1, m) - _fib_births(n - 1, m)

@memoize
def _fib_deaths(n, m):
    return _fib_births(n - m, m)


def main(input_string):
    n, m = map(int, input_string.split())
    print(fib_with_mortality(n, m))


if __name__ == '__main__':
    main(rosalind_input())
