# COUNT ONES IN BINARY REPRESENTATION
# The count_ones function counts the number of ones
# in the binary representation of an integer.

def count_ones(n): return bin(n).count('1')
result = count_ones(12)
print(result)
# Output: 2