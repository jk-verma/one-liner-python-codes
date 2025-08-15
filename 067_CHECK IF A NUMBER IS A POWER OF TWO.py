# CHECK IF A NUMBER IS A
# POWER OF TWO
# The
# IsPowerOfTwo
# function
# checks
# whether a given number is a power of two
# using bitwise operations.
def IsPowerOfTwo(num): return num & (num - 1) == 0
# Example usage
print(IsPowerOfTwo(16))
# Output: True (16 is 2^4)
print(IsPowerOfTwo(5))
# Output: False