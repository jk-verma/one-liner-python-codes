'''
Problem    : GENERATE A RANDOM NUMBER WITHIN A RANGE
Description: The random_in_range function generates a random number within the specified range.
@Author    : Dr. J. K. Verma
@Date      : 2025-08-15
@Version   : 1.0
'''

import random
def random_in_range(min_val, max_val): return random.randint(min_val, max_val)
print(random_in_range(1, 10))
# Output: e.g., 6