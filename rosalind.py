import sys

from collections import Counter
from abc import ABC, abstractmethod
from functools import wraps


def memoize(func):
    cache = {}

    @wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return wrapper


def rosalind_input():
    """Open a scripts first input file as a string."""
    try:
        with open(sys.argv[1]) as input_file:
            return input_file.read().strip()
    except (IndexError, IOError) as e:
        print(f'Error: {e}.')
        print('You must specify an input file.', file=sys.stderr)
        sys.exit(1)


def parse_fasta(input_string, datatype=str):
    """Parse a string in the FASTA format.

    The string may contain multiple DNA strings, each with a name. Each
    name/DNA pair consists of one line starting with '>', the rest of which is
    the name, followed by any number of lines containing the DNA sequence.
    """
    curr_name = None
    dataset = {}

    for line in input_string.strip().split('\n'):
        if line[0] == '>':
            curr_name = line[1:]
            dataset[curr_name] = []
        else:
            dataset[curr_name].append(line)

    return {name: datatype(''.join(seq)) for name, seq in dataset.items()}


class BasePairString(str, ABC):
    """Abstract base class for DNA and RNA, containing operations that can be applied
    to both."""

    @classmethod
    @abstractmethod
    def _complement_table(cls):
        pass

    def gc_count(self):
        """The fraction of base pairs that are either G or C."""
        counts = Counter(self)
        return (counts['G'] + counts['C']) / len(self)

    def complement(self):
        """The complement of a base pair string."""
        return self.translate(self.complement_table())

    def reverse_complement(self):
        """The reverse complement of a base pair string."""
        return self.complement()[::-1]

    def hamming_distance(self, other):
        """The number of characters that are different between this string and
        another string of equal length."""
        return sum(1 for a, b in zip(self, other) if a != b)


class DNA(BasePairString):
    _rna_table = str.maketrans('T', 'U')
    _complement_table = str.maketrans('ACGT', 'TGCA')

    @classmethod
    def complement_table(cls):
        return cls._complement_table

    def to_rna(self):
        """Convert DNA to RNA by replacing T with U."""
        return RNA(self.translate(DNA._rna_table))


class RNA(BasePairString):
    _dna_table = str.maketrans('U', 'T')
    _complement_table = str.maketrans('ACGU', 'UGCA')
    _codons = {
        'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
        'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
        'UAU': 'Y', 'UAC': 'Y', 'UAA': '*', 'UAG': '*',
        'UGU': 'C', 'UGC': 'C', 'UGA': '*', 'UGG': 'W',
        'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
        'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
        'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
        'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
        'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M',
        'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
        'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
        'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
        'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
        'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
        'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
        'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G',
    }

    @classmethod
    def complement_table(cls):
        return cls._complement_table

    def to_dna(self):
        """Convert RNA to DNA by replacing U with T."""
        return RNA(self.translate(RNA._dna_table))

    def to_protein(self):
        amino_acids = []
        for idx in range(0, len(self), 3):
            aa = RNA._codons[self[idx:idx+3]]
            if aa != '*':
                amino_acids.append(aa)
            else:
                break
        return Protein(''.join(amino_acids))

    def to_amino_acids(self):
        return ''.join(RNA._codons[self[idx:idx+3]] for idx in range(0, len(self) - len(self) % 3, 3))


class Protein(str):
    _aa_masses = {
        'A': 71.03711,
        'C': 103.00919,
        'D': 115.02694,
        'E': 129.04259,
        'F': 147.06841,
        'G': 57.02146,
        'H': 137.05891,
        'I': 113.08406,
        'K': 128.09496,
        'L': 113.08406,
        'M': 131.04049,
        'N': 114.04293,
        'P': 97.05276,
        'Q': 128.05858,
        'R': 156.10111,
        'S': 87.03203,
        'T': 101.04768,
        'V': 99.06841,
        'W': 186.07931,
        'Y': 163.06333
    }
