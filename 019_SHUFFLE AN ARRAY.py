# SHUFFLE AN ARRAY

# The shuffle_array function randomly
# shuffles the elements of a given array.

import random

def shuffle_array(arr):
    shuffled = arr[:]
    random.shuffle(shuffled)
    return shuffled

print(", ".join(map(str, shuffle_array([1, 2, 3, 4]))))
# Output: e.g., 4, 2, 3, 1