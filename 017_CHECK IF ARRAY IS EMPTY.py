# CHECK IF ARRAY IS EMPTY

# The is_not_empty function checks if an
# array is not empty.
def is_not_empty(arr): return isinstance(arr, list) and len(arr) > 0

print(is_not_empty([1, 2, 3]))
# Output: True