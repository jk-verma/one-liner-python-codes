'''
Problem    : FIND THE NTH FIBONACCI NUMBER (RECURSIVE)
Description: The fibonacci function finds the nth fibonacci number (recursive).
@Author    : Dr. J. K. Verma
@Date      : 2025-09-20
'''

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
# Example usage:
n = 7
result = fibonacci(n)
print(f"Output: {result}")
# Output: 13