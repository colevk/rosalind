#!/usr/bin/env python3


"""
Given: A DNA string of length at most 1 kbp in FASTA format.

Return: The position and length of every reverse palindrome in the string
having length between 4 and 12. You may return these pairs in any order.
"""

from rosalind import *


if __name__ == '__main__':
    sequence = list(parse_fasta(rosalind_input()).values())[0]
    sequence_length = len(sequence)
    for offset in range(sequence_length):
        for length in range(4, 14, 2):
            if offset + length > sequence_length:
                continue
            palindrome = DNA(sequence[offset:offset+length])
            if palindrome == palindrome.reverse_complement():
                print(offset + 1, length)
