# FIND THE MINIMUM AND MAXIMUM NUMBERS IN AN ARRAY

# The min_max function finds the minimum and maximum numbers in an array.

def min_max(arr):
    return min(arr), max(arr)
# Example usage
result = min_max([10, 5, 25, 3, 15])
print(f"{{ min: {result[0]}, max: {result[1]} }}")
# Output: { min: 3, max: 25 }