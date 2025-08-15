# CHECK IF A NUMBER IS A FIBONACCI NUMBER

# The IsFibonacci function checks if a number is a Fibonacci number.

def IsFibonacci(num):
    return IsPerfectSquare(5 * num * num + 4) or IsPerfectSquare(5 * num * num - 4)
def IsPerfectSquare(num):
    sqrt = int(num ** 0.5)
    return sqrt * sqrt == num
# Example usage
print(IsFibonacci(5))
# True
print(IsFibonacci(6))
# False