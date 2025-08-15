# CALCULATE PI TO N DECIMAL PLACES

# The my_pi function takes an integer n and returns the mathematical constant PI to n
# decimal places.

import math
def my_pi(n):
    return round(math.pi, n)
# Example usage
print(my_pi(5))
# Output: 3.14159