# Given positive integers n <= 40
# and k <= 5
# Return the total number of rabbit
# pairs that will be present after
# n months, if we begin with 1 pair
# and in each generation, every pair
# of reproduction-age rabbits produces
# a litter of k rabbit pairs

import sys
from pathlib import Path
from re import findall

rabbit_dict = {1: 1,
               2: 1}


def rabbits(n, k):
    global rabbit_dict
    if n not in rabbit_dict.keys():
        temp = rabbits(n-2, k)*k + rabbits(n-1, k)
        rabbit_dict.update({n: temp})
    return rabbit_dict[n]


if __name__ == '__main__':
    filepath = Path(sys.argv[1])
    with open(filepath) as data:
        line = data.readline()
        vals = findall(r'\d+', line)
        n = int(vals[0])
        k = int(vals[1])
        for i in range(1, n+1):
            rabbits(i, k)
        print(rabbits(n, k))
