# GENERATE A RANDOM NUMBER WITHIN A RANGE
#
# The random_in_range function generates a random number within the specified range.

import random
def random_in_range(min_val, max_val): return random.randint(min_val, max_val)
print(random_in_range(1, 10))
# Output: e.g., 6