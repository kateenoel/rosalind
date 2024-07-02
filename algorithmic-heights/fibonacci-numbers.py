# Given a positive integer n >= 25
# Return the value of F_n

import sys
from pathlib import Path

fib_dict = {0: 0,
            1: 1}


def fibonacci(n):
    global fib_dict
    if n not in fib_dict.keys():
        temp = fibonacci(n-1) + fibonacci(n-2)
        fib_dict.update({n: temp})
    return fib_dict[n]


if __name__ == '__main__':
    filepath = Path(sys.argv[1])
    n = int(filepath.read_text())
    for i in range(n+1):
        fibonacci(i)
    print(fibonacci(n))
