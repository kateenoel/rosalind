# Given a DNA string s of length at most 1000 nt
# Return four integers (separated by spaces) counting
# the respective number of times that the symbols
# 'A', 'C'. 'G', and 'T' occur in s


def main():
    with open('data.txt') as fs:
        dna = fs.read()

    countA = dna.count('A')
    countC = dna.count('C')
    countG = dna.count('G')
    countT = dna.count('T')

    print(countA, countC, countG, countT)


if __name__ == '__main__':
    main()
