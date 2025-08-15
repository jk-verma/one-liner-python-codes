# FIND THE INDEX OF AN ELEMENT IN AN ARRAY

# The find_index function finds the index of an element in an array.

def find_index(arr, element):
    try:
        return arr.index(element)
    except ValueError:
        return -1
# Example usage
fruits = ["apple", "banana", "orange", "grape"]
print(find_index(fruits, "orange"))
# Output: 2