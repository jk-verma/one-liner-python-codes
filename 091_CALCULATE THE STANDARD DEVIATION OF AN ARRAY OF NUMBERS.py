# CALCULATE THE STANDARD DEVIATION OF AN ARRAY OF NUMBERS

# The standard_deviation function calculates the standard deviation of an array of numbers.

import math
def standard_deviation(arr):
    mean = sum(arr) / len(arr)
    sum_of_squared_differences = sum((x - mean) ** 2 for x in arr)
    return math.sqrt(sum_of_squared_differences / len(arr))
# Example usage
print(standard_deviation([1, 2, 3, 4, 5]))
# Output: 1.4142135623730951