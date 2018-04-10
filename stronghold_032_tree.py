#!/usr/bin/env python3

"""
Given: A positive integer n (n≤1000) and an adjacency list corresponding to a
graph on n nodes that contains no cycles.

Return: The minimum number of edges that can be added to the graph to produce
a tree.

>>> main('''10
... 1 2
... 2 8
... 4 10
... 5 9
... 6 10
... 7 9''')
3
"""

from rosalind import *


def main(input_string):
    lines = input_string.split('\n')
    nodes = int(lines[0])
    edges = len(lines) - 1
    print(nodes - edges - 1)


if __name__ == '__main__':
    main(rosalind_input())
