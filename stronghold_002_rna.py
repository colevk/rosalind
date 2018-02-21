#!/usr/bin/env python3

'''
Given: A DNA string t having length at most 1000 nt.

Return: The transcribed RNA string of t.
'''

from rosalind import *

if __name__ == '__main__':
    dna = DNA(rosalind_input())
    print(dna.to_rna())
