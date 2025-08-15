# GET THE LAST N ELEMENTS
# OF AN ARRAY
# The LastNElements function retrieves the
# last n elements of an array.
def LastNElements(arr, n):
    return arr[-n:]
# Example usage
result = LastNElements([1, 2, 3, 4, 5], 3)
print(", ".join(map(str, result)))
# Output: 3, 4, 5