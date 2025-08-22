'''
Problem    : REMOVE NULL VALUES FROM A LIST.
Description: The remove_null function removes null values from a list.
@Author    : Dr. J. K. Verma
@Date      : 2025-09-20
'''
def remove_null(arr):
    return [item for item in arr if item is not None]
# Example usage
array = [1, None, 2, 3, None, 4, None]
result = remove_null(array)
print(f"Output: {result}")
# Output: [1, 2, 3, 4]