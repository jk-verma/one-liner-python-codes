'''
Problem    : CALCULATE THE SUM OF CUBES OF AN ARRAY
Description: The sum_of_cubes function calculates the sum of cubes of an array.
@Author    : Dr. J. K. Verma
@Date      : 2025-09-20
'''
def sum_of_cubes(arr):
    return sum(x ** 3 for x in arr)
# Example usage:
arr = [1, 2, 3, 4, 5]
sum_result = sum_of_cubes(arr)
print(f"Output: {sum_result}")
# Output: 225