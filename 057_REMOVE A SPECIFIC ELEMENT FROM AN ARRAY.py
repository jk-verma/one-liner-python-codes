# REMOVE A SPECIFIC ELEMENT FROM AN ARRAY

# The remove_element function removes a
# specific element from an array.
def remove_element(arr, element):
    return [x for x in arr if x != element]
# Example usage
result = remove_element([1, 2, 3, 4, 5], 3)
print(result)
# Output: [1, 2, 4, 5]