#!/usr/bin/env python3

"""
Given: The UniProt ID of a protein.

Return: A list of biological processes in which the protein is involved
(biological processes are found in a subsection of the protein's "Gene
Ontology" (GO) section).

>>> main('Q5SLP9')
DNA recombination
DNA repair
DNA replication
"""

from rosalind import rosalind_input
from Bio import ExPASy
from Bio import SwissProt


def main(input_string):
    record = SwissProt.read(ExPASy.get_sprot_raw(input_string))
    for ref in record.cross_references:
        if ref[0] == 'GO' and ref[2].startswith('P:'):
            # if reference is a Gene Ontology reference and refers to a
            # biological process
            print(ref[2][2:])


if __name__ == '__main__':
    main(rosalind_input())
