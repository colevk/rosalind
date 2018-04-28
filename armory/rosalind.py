import sys


def rosalind_input():
    """Open a script's first input file as a string."""
    try:
        with open(sys.argv[1]) as input_file:
            return input_file.read().strip()
    except (IndexError, IOError) as e:
        print(f'Error: {e}.')
        print('You must specify an input file.', file=sys.stderr)
        sys.exit(1)