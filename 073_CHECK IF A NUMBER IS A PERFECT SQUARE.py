# CHECK IF A NUMBER IS A PERFECT SQUARE

# The IsPerfectSquare function checks if a given number is a perfect square.

def IsPerfectSquare(num):
    sqrt = num ** 0.5
    return sqrt.is_integer()
# Example usage
print(IsPerfectSquare(16))
# Output: True
print(IsPerfectSquare(10))
# Output: False