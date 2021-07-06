# Given six nonnegative integers, each of which does not exceed
# 20,000. The integers correspond to the number of couples in a
# population possessing each genotype pairing for a given factor.
# In order, the six given integers represent the number of couples
# having the following genotypes:
# 1. AA-AA
# 2. AA-Aa
# 3. AA-aa
# 4. Aa-Aa
# 5. Aa-aa
# 6. aa-aa
# Return the expected number of offspring displaying the dominant
# phenotype in the next generation, under the assumption that every
# couple has exactly two offspring

import sys
from pathlib import Path

if __name__ == '__main__':
    filepath = Path(sys.argv[1])
    population = filepath.read_text()
    population = population.replace('\n', '')
    popVals = population.split(' ')
    popValsInt = [int(i) for i in popVals]

    numOffspring = int(popValsInt[0]*2 + popValsInt[1]*2 + popValsInt[2]*2 + popValsInt[3]*1.5 + popValsInt[4]*1 + popValsInt[5]*0)
    print(numOffspring)