# Given a DNA string t having length at most 1000 nt
# Return the transcribed RNA string of t


def main():
    with open('data.txt') as fs:
        dna = fs.read()

    rna = dna.replace('T', 'U')

    print(rna)


if __name__ == '__main__':
    main()