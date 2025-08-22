'''
Problem    : MAXIMUM TRIANGLE EDGE CALCULATOR
Description: The next_edge function provides a concise function for determining the maximum
             possible length of the third edge of a triangle, given the lengths of the other
             two sides as integers.
@Author    : Dr. J. K. Verma
@Date      : 2025-09-20
'''

def next_edge(side1, side2):
    return side1 + side2 - 1
side1 = 5
side2 = 7
print(next_edge(side1, side2))
# Output: 11