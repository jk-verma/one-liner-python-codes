'''
Problem    : ONE-LINER BITWISE OPERATIONS IN PYTHON
Description: These bitwise_and, bitwise_or, and bitwise_xor functions work similarly to the lambda expressions but use the def keyword for function definition. They take two integers n1 and n2 as input and return the result of the respective bitwise AND, OR, and XOR operations between them.
@Author    : Dr. J. K. Verma
@Date      : 2025-09-20
'''

def bitwise_and(n1, n2):
    return n1 & n2
def bitwise_or(n1, n2):
    return n1 | n2
def bitwise_xor(n1, n2):
    return n1 ^ n2
num1, num2 = 5, 3
print(bitwise_and(num1, num2)) # Output: 1
print(bitwise_or(num1, num2)) # Output: 7
print(bitwise_xor(num1, num2)) # Output: 6