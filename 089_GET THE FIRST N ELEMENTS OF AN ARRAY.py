# GET THE FIRST N ELEMENTS OF AN ARRAY

# The FirstNElements function get the first n elements of an array.

def FirstNElements(arr, n): return arr[:n]
# Use list slicing to retrieve the first n elements of the array

# Example usage
array = [1, 2, 3, 4, 5]
first_n_elements = FirstNElements(array, 3)
print(", ".join(map(str, first_n_elements)))
# Output: 1, 2, 3