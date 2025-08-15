# CHECK IF AN ARRAY IS SORTED IN DESCENDING ORDER

# The sorted_descending function checks if an array is sorted in descending order.

def sorted_descending(arr):
    return all(arr[i] >= arr[i + 1] for i in range(len(arr) - 1))
# Example usage
print(sorted_descending([5, 4, 3, 2, 1]))
# Output: True
print(sorted_descending([1, 5, 3, 8, 2]))
# Output: False