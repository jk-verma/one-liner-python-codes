# VALIDATE NUMBER WITHIN BOUNDS

# The int_within_bounds function validates whether a number n is exclusively within
# the bounds of lower and upper.

def int_within_bounds(n, lower, upper): return lower <= n < upper and n % 1 == 0
print(int_within_bounds(10, 5, 20))
# Output: True
print(int_within_bounds(5, 5, 20))
# Output: False
print(int_within_bounds(21, 5, 20))
# Output: False