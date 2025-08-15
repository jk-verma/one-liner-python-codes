# FIND THE DIFFERENCE BETWEEN TWO ARRAYS

# The ArrayDifference function finds the
# difference between two arrays.

def ArrayDifference(arr1, arr2):
    return list(set(arr1) - set(arr2))
# Example usage
arr1 = [1, 2, 3]
arr2 = [2, 3, 4]
difference = ArrayDifference(arr1, arr2)
print(", ".join(map(str, difference)))
# Output: 1