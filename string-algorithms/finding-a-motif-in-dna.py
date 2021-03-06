# Given two DNA strings s and t (each of length at
# most 1 kbp)
# Return all locations of t as a substring of s

import sys
from pathlib import Path

if __name__ == '__main__':
    filepath = Path(sys.argv[1])
    with open(filepath) as data:
        main = data.readline()
        for line in data:
            pass
        sub = line.replace('\n', '')

    indices = [i for i in range(len(main)) if main.startswith(sub, i)]
    indices = [x + 1 for x in indices]

    print(*indices, sep = ' ')