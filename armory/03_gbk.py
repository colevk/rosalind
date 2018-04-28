#!/usr/bin/env python3

"""
Given: A genus name, followed by two dates in YYYY/M/D format.

Return: The number of Nucleotide GenBank entries for the given genus that were
published between the dates specified.

>>> main('''Anthoxanthum
... 2003/7/25
... 2005/12/27''')
7
"""

import subprocess
from rosalind import rosalind_input
from Bio import Entrez


def query_string(organism, start_date, end_date):
    return f'"{organism}"[Organism] AND ("{start_date}"[PDAT] : "{end_date}"[PDAT])'


def main(input_string):
    organism, start_date, end_date = input_string.split('\n')
    Entrez.email = subprocess.check_output(['git', 'config', 'user.email']).decode().strip()
    record = Entrez.read(Entrez.esearch('nucleotide', query_string(organism, start_date, end_date)))
    print(record["Count"])


if __name__ == '__main__':
    main(rosalind_input())
