# CHECK IF AN ARRAY IS A SUBSET OF ANOTHER ARRAY

# The is_subset function checks if an array is a subset of another array.

def is_subset(arr1, arr2):
    return all(item in arr2 for item in arr1)
# Example usage
print(is_subset([1, 2, 3], [2, 3, 4, 5, 6]))
# Output: False
print(is_subset([1, 2, 3], [2, 3, 1, 5, 6]))
# Output: True