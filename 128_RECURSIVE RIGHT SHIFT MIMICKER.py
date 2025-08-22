'''
Problem    : RECURSIVE RIGHT SHIFT MIMICKER
Description: The shift_to_right function employs recursion to repeatedly divide the first integer by 2 y times, emulating the right shift operation. This approach offers a compact and elegant solution for performing right shifts between two given integers.
@Author    : Dr. J. K. Verma
@Date      : 2025-09-21
'''


def shift_to_right(x, y):
    return x if y < 1 else shift_to_right(x // 2, y - 1)
x = 16
y = 2
print(shift_to_right(x, y))
# Output: 4