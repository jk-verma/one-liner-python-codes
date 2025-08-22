'''
Problem    : CHECK IF A NUMBER IS A NEON NUMBER
Description: The is_neon_number function checks if a number is a neon number.
@Author    : Dr. J. K. Verma
@Date      : 2025-09-20
'''

def is_neon_number(num):
    sum_of_digits = 0
    square = num * num
    while square:
        sum_of_digits += square % 10
        square //= 10
    return sum_of_digits == num
print(is_neon_number(9))
# Output: True