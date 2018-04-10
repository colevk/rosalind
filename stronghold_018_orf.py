#!/usr/bin/env python3

"""
Given: A DNA string s of length at most 1 kbp in FASTA format.

Return: Every distinct candidate protein string that can be translated from
ORFs of s. Strings can be returned in any order.

>>> main('''>Rosalind_99
... AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG''')
M
MGMTPRLGLESLLE
MLLGSFRLIPKETLIQVAGSSPCNLS
MTPRLGLESLLE
"""

from rosalind import *
import regex

VALID_PROTEIN = 'M[^*]*\*'


def main(input_string):
    dna = next(iter(parse_fasta(input_string).values()))
    dna_revc = DNA(dna).reverse_complement()
    frames = [
        DNA(dna).to_rna().to_amino_acids(),
        DNA(dna[1:]).to_rna().to_amino_acids(),
        DNA(dna[2:]).to_rna().to_amino_acids(),
        DNA(dna_revc).to_rna().to_amino_acids(),
        DNA(dna_revc[1:]).to_rna().to_amino_acids(),
        DNA(dna_revc[2:]).to_rna().to_amino_acids()
    ]
    matches = set()
    for frame in frames:
        matches.update(regex.findall(VALID_PROTEIN, frame, overlapped=True))
    for match in sorted(matches):
        print(match[:-1])


if __name__ == '__main__':
    main(rosalind_input())
