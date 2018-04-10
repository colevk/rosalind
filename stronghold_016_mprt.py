#!/usr/bin/env python3

"""
Given: At most 15 UniProt Protein Database access IDs.

Return: For each protein possessing the N-glycosylation motif, output its
given access ID followed by a list of locations in the protein string where
the motif can be found.

>>> main('''A2Z669
... B5ZC00
... P07204_TRBM_HUMAN
... P20840_SAG1_YEAST''')
B5ZC00
85 118 142 306 395
P07204_TRBM_HUMAN
47 115 116 382 409
P20840_SAG1_YEAST
79 109 135 248 306 348 364 402 485 501 614
"""

from rosalind import *

import requests
import regex


N_GLYCOSYLATION_MOTIF = 'N[^P][ST][^P]'


def get_protein(id):
    fasta_raw = requests.get('http://www.uniprot.org/uniprot/{}.fasta'.format(id)).text
    return next(iter(parse_fasta(fasta_raw).values()))


def find_motif(motif, protein):
    return [match.span()[0] for match in regex.finditer(motif, protein, overlapped=True)]


def main(input_string):
    for id in input_string.split():
        matches = find_motif(N_GLYCOSYLATION_MOTIF, get_protein(id))
        if len(matches) > 0:
            print(id)
            print(' '.join(str(idx + 1) for idx in matches))


if __name__ == '__main__':
    main(rosalind_input())
