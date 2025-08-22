'''
Problem    : CHECK IF ARRAY IS EMPTY
Description: The is_not_empty function checks if an array is not empty.
@Author    : Dr. J. K. Verma
@Date      : 2025-08-15
@Version   : 1.0
'''

def is_not_empty(arr): return isinstance(arr, list) and len(arr) > 0

print(is_not_empty([1, 2, 3]))
# Output: True