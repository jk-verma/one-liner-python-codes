'''
Problem    : SUM OF INDEX MULTIPLIED ELEMENTS
Description: The index_multiplier function calculates the sum of all items in an array, where each
             item is multiplied by its index (zero-based). If the array is empty, it returns 0.
@Author    : Dr. J. K. Verma
@Date      : 2025-08-15
@Version   : 1.0
'''

def index_multiplier(arr): return sum(value * index for
index, value in enumerate(arr))
arr = [1, 2, 3, 4, 5]
print(index_multiplier(arr))
# Output: 40