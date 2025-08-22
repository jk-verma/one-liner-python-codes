'''
Problem    : SYMMETRY CHECKER
Description: The is_symmetrical function determines whether a given integer is symmetrical,
             meaning it reads the same backward as forward.
@Author    : Dr. J. K. Verma
@Date      : 2025-09-20
'''

def is_symmetrical(num):
    return str(num) == str(num)[::-1]
num = 12321
print(is_symmetrical(num))
# Output: True