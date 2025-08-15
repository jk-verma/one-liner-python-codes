# GENERATE A FIBONACCI SEQUENCE

# The Fibonacci generates a Fibonacci sequence.

def Fibonacci(n):
    return n if n <= 1 else Fibonacci(n - 1) + Fibonacci(n - 2)
# Example usage
fibonacci_sequence = [Fibonacci(i) for i in range(8)]
print(', '.join(map(str, fibonacci_sequence)))
# Output: 0, 1, 1, 2, 3, 5, 8, 13