# Given a DNA string s of length at most 1000 bp
# Return the reverse complement s^c of s

import sys

def main():
    with open(sys.argv[1]) as fs:
        dna = fs.read()

    complements = {'A': 'T', 'C': 'G', 'T': 'A', 'G': 'C'}

    reverse = dna[::-1]

    reverse = reverse.lstrip()

    reverseComplement = ''

    for base in reverse:
        reverseComplement += complements[base]

    print(reverseComplement)


if __name__ == '__main__':
    main()