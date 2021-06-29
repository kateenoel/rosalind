# Given three positive integers k, m, and n, representing
# a population containing k + m + n organisms, k individuals
# are homozygous dominant for a factor, m are heterozygous,
# and n are homozygous recessive
# Return the probability that two randomly selected mating
# organisms will produce an individual possessing a
# dominant allele (and thus displaying the dominant phenotype).
# Assume that any two organisms can mate

import sys
from pathlib import Path
from re import findall

if __name__ == '__main__':
    filepath = Path(sys.argv[1])
    with open(filepath) as data:
        line = data.readline()
        line = line.replace('\n', '')

    vals = findall(r'\d+', line)
    k = int(vals[0])
    m = int(vals[1])
    n = int(vals[2])
    total = k + m + n

    # probability tree
    probKK = (k/total)*((k-1)/(total-1))
    probKM = (k/total)*(m/(total-1))
    probKN = (k/total)*(n/(total-1))
    probMK = (m/total)*(k/(total-1))
    probMM = (m/total)*((m-1)/(total-1))
    probMN = (m/total)*(n/(total-1))
    probNK = (n/total)*(k/(total-1))
    probNM = (n/total)*(m/(total-1))
    probNN = (n/total)*((n-1)/(total-1))

    # probability of having a dominant allele
    probDomKK = 1
    probDomKM = 1
    probDomKN = 1
    probDomMK = 1
    probDomMM = 3/4
    probDomMN = 1/2
    probDomNK = 1
    probDomNM = 1/2
    probDomNN = 0

    # compute total probability
    prob = probKK*probDomKK + probKM*probDomKM + probKN*probDomKN + probMK*probDomMK + probMM*probDomMM + probMN*probDomMN + probNK*probDomNK + probNM*probDomNM + probNN*probDomNN
    print(prob)
