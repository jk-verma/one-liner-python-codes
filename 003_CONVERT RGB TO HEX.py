'''
Problem    : CONVERT RGB TO HEX
Description: The rgb_to_hex function combines the red, green, and blue (RGB) values into a single hexadecimal color code
@Author    : Dr. J. K. Verma
@Date      : 2025-08-15
@Version   : 1.0
'''


def rgb_to_hex(r, g, b): return f"#{((r << 16) + (g << 8) + 
                                     b):06X}"
print(rgb_to_hex(0, 51, 255))
# Output: #0033FF