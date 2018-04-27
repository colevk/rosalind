#!/usr/bin/env python3

"""
After identifying the exons and introns of an RNA string, we only need to
delete the introns and concatenate the exons to form a new string ready for
translation.

Given: A DNA string s (of length at most 1 kbp) and a collection of substrings
of s acting as introns. All strings are given in FASTA format.

Return: A protein string resulting from transcribing and translating the exons
of s. (Note: Only one solution will exist for the dataset provided.)

>>> main('''>Rosalind_10
... ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG
... >Rosalind_12
... ATCGGTCGAA
... >Rosalind_15
... ATCGGTCGAGCGTGT''')
MVYIADKQHVASREAYGHMFKVCA
"""


from rosalind import *


def main(input_string):
    dna_strings = [v for _, v in parse_fasta(input_string)]
    main_string = dna_strings[0]
    for intron in dna_strings[1:]:
        main_string = main_string.replace(intron, '')
    print(DNA(main_string).to_rna().to_protein())


if __name__ == '__main__':
    main(rosalind_input())
