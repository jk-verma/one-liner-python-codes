# CHECK IF AN ARRAY # CONTAINS A SPECIFIC VALUE

# The contains_value function checks if a
# given array contains a specific value.

def contains_value(arr, value): return value in arr
# Example usage
print(contains_value([1, 2, 3, 4, 5], 3))
# Output: True
print(contains_value([1, 2, 3, 4, 5], 6))
# Output: False