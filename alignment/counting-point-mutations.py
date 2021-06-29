# Given two DNA strings s and t of equal length
# (not exceeding 1 kbp)
# Return the Hamming distance d_H(s,t)

import sys
from pathlib import Path

if __name__ == '__main__':
    filepath = Path(sys.argv[1])
    with open(filepath) as data:
        first = data.readline()
        for line in data:
            pass
        second = line

    dist = 0
    for i in range(len(first)):
        if first[i] != second[i]:
            dist += 1

    print(dist)