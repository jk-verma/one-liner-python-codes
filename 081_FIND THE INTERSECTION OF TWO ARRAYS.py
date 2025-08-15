# FIND THE INTERSECTION OF TWO ARRAYS

# The FindIntersection function finds the intersection of two arrays.

def FindIntersection(arr1, arr2):
    return list(set(arr1) & set(arr2))
# Example usage
arr1 = [1, 2, 3]
arr2 = [2, 3, 4]
intersection = FindIntersection(arr1, arr2)
print(intersection)
# Output: [2, 3]