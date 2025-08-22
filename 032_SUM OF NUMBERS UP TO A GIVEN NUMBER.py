'''
Problem    : SUM OF NUMBERS UP TO A GIVEN NUMBER
Description: The add_up function calculates the sum of all numbers from 1 to the number passed to the function in C#.
@Author    : Dr. J. K. Verma
@Date      : 2025-08-15
@Version   : 1.0
'''


def add_up(num): return num * (num + 1) // 2
print(add_up(5))
# Output: 15