'''
Problem    : CHECK IF A NUMBER IS A DISARIUM NUMBER
Description: The is_disarium_number function checks if a number is a disarium number.
@Author    : Dr. J. K. Verma
@Date      : 2025-08-25
'''

from turtledemo.clock import current_day
def is_disarium_number(num):
    num_str = str(num)
    disarium_sum = sum(int(digit) ** (i + 1) for i, digit in enumerate(num_str))
    return disarium_sum == num
# Test cases
print(is_disarium_number(89))
# Output: True
print(is_disarium_number(135))
# Output: True
print(is_disarium_number(23))
# Output: False