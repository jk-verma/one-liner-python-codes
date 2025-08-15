# CHECK IF AN ARRAY IS SORTED IN ASCENDING ORDER

# The is_sorted_ascending function takes an array arr as input and checks if every element in
# the array is greater than or equal to the previous element, ensuring that the array is
# sorted in ascending order.

def is_sorted_ascending(arr):
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))
# Example usage
print(is_sorted_ascending([1, 2, 3, 5, 8]))
# Output: True
print(is_sorted_ascending([1, 5, 3, 8, 2]))
# Output: False