# SIMPLE CALCULATOR

# The calculator function calculates different operations.

def calculator(num1, op, num2):
    return {'+': num1 + num2, '-': num1 - num2, '*': num1 *  num2, '/': num1 / num2}[op]
# Example usage
print(calculator(5, '+', 3)) # Addition outputs: 8
print(calculator(10, '-', 4)) # Subtraction outputs: 6
print(calculator(6, '*', 2)) # Multiplication outputs: 12
print(calculator(20, '/', 5)) # Division outputs: 4