'''
Problem    : COUNT ONES IN BINARY REPRESENTATION
Description: The count_ones function counts the number of ones in the binary representation of an integer.
@Author    : Dr. J. K. Verma
@Date      : 2025-08-15
@Version   : 1.0
'''

def count_ones(n): return bin(n).count('1')
result = count_ones(12)
print(result)
# Output: 2