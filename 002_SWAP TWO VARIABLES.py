# SWAP TWO VARIABLES

# The swap_without_temp function swaps the values of two variables a and b without using
# a temporary variable.

def swap_without_temp(a, b):
    return b, a
result = swap_without_temp(5, 10)
print(f"After swapping: a = {result[1]}, b = {result[0]}")
# Output: After swapping: a = 10, b = 5