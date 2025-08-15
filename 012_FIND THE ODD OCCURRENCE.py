# FIND THE ODD OCCURRENCE

# The find_odd function finds the integer
# which appears an odd number of times in a
# given list of integers.

import random
import functools

def find_odd(ar):
    return functools.reduce(lambda x, y: x ^ y, ar)

ar = [random.randint(1, 100) for _ in range(random.randint(10, 20))]
print("Input:", " ".join(map(str, ar)))
print("Result:", find_odd(ar))
# Input: 25 32 37 63 66 6 4 26 2 38 59 1 30
# Result: 121