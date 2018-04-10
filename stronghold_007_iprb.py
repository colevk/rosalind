#!/usr/bin/env python3

"""
Given: Three positive integers k, m, and n, representing a population
containing k+m+n organisms: k individuals are homozygous dominant for a factor,
m are heterozygous, and n are homozygous recessive.

Return: The probability that two randomly selected mating organisms will
produce an individual possessing a dominant allele (and thus displaying the
dominant phenotype). Assume that any two organisms can mate.

>>> main('2 2 2')
0.78333
"""

from rosalind import *


def dominant_allele_probability(k, m, n):
    total = k + m + n
    return (
        k / total +
        m / total * 0.5 +
        m / total * 0.5 * k / (total - 1) +
        m / total * 0.5 * (m - 1) / (total - 1) * 0.5 +
        n / total * k / (total - 1) +
        n / total * m / (total - 1) * 0.5
    )


def main(input_string):
    alleles = map(int, input_string.split())
    print('{:.5f}'.format(dominant_allele_probability(*alleles)))


if __name__ == '__main__':
    main(rosalind_input())
