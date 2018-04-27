#!/usr/bin/env python3

"""
Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp)
in FASTA format.

Return: A consensus string and profile matrix for the collection. (If several
possible consensus strings exist, then you may return any one of them.)

>>> main('''>Rosalind_1
... ATCCAGCT
... >Rosalind_2
... GGGCAACT
... >Rosalind_3
... ATGGATCT
... >Rosalind_4
... AAGCAACC
... >Rosalind_5
... TTGGAACT
... >Rosalind_6
... ATGCCATT
... >Rosalind_7
... ATGGCACT''')
ATGCAACT
A: 5 1 0 0 5 5 0 0
C: 0 0 1 4 2 0 6 1
G: 1 1 6 3 0 1 0 0
T: 1 5 0 0 0 1 1 6
"""

from rosalind import *


class Consensus:
    def __init__(self, sequences):
        it = iter(sequences)
        first = next(it)
        self._length = len(first)
        self.profile = {
            'A': [0] * self._length,
            'C': [0] * self._length,
            'G': [0] * self._length,
            'T': [0] * self._length,
        }
        self._update_profile(first)
        for sequence in it:
            self._update_profile(sequence)
        self._update_consensus_string()

    def _update_profile(self, sequence):
        for idx, bp in enumerate(sequence):
            self.profile[bp][idx] += 1

    def _update_consensus_string(self):
        self.consensus_string = ''.join(
            max('ACGT', key=lambda k: self.profile[k][idx])
            for idx in range(self._length)
        )

    def update(self, sequence):
        self._update_profile(sequence)
        self._update_consensus_string()


def main(input_string):
    dna_strings = parse_fasta(input_string)
    consensus = Consensus(v for _, v in dna_strings)
    print(consensus.consensus_string)
    for bp in 'ACGT':
        print('{}: {}'.format(bp, ' '.join(map(str, consensus.profile[bp]))))


if __name__ == '__main__':
    main(rosalind_input())
