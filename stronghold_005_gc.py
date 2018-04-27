#!/usr/bin/env python3

"""
Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

Return: The ID of the string having the highest GC-content, followed by the
GC-content of that string. Rosalind allows for a default error of 0.001 in all
decimal answers unless otherwise stated; please see the note on absolute error
below.

>>> main('''>Rosalind_6404
... CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
... TCCCACTAATAATTCTGAGG
... >Rosalind_5959
... CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
... ATATCCATTTGTCAGCAGACACGC
... >Rosalind_0808
... CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
... TGGGAACCTGCGGGCAGTAGGTGGAAT''')
Rosalind_0808
60.919540
"""

from rosalind import *


def main(input_string):
    dataset = dict(parse_fasta(input_string, datatype=DNA))
    key = max(dataset, key=lambda x: dataset[x].gc_count())
    print(key)
    print('{:.6f}'.format(dataset[key].gc_count() * 100))


if __name__ == '__main__':
    main(rosalind_input())
