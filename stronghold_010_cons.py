#!/usr/bin/env python3

"""
Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp)
in FASTA format.

Return: A consensus string and profile matrix for the collection. (If several
possible consensus strings exist, then you may return any one of them.)
"""

from rosalind import *


class Consensus:
    def __init__(self, sequences):
        self._length = len(sequences[0])
        self.profile = {
            'A': [0] * self._length,
            'C': [0] * self._length,
            'G': [0] * self._length,
            'T': [0] * self._length,
        }
        for sequence in sequences:
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


if __name__ == '__main__':
    dna_strings = parse_fasta(rosalind_input())
    consensus = Consensus(list(dna_strings.values()))
    print(consensus.consensus_string)
    for bp in 'ACGT':
        print('{}: {}'.format(bp, ' '.join(map(str, consensus.profile[bp]))))
