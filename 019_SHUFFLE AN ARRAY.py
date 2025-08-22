'''
Problem    : SHUFFLE AN ARRAY
Description: The shuffle_array function randomly shuffles the elements of a given array.
@Author    : Dr. J. K. Verma
@Date      : 2025-08-15
@Version   : 1.0
'''

import random

def shuffle_array(arr):
    shuffled = arr[:]
    random.shuffle(shuffled)
    return shuffled

print(", ".join(map(str, shuffle_array([1, 2, 3, 4]))))
# Output: e.g., 4, 2, 3, 1