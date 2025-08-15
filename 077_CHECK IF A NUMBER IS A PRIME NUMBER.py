# CHECK IF A NUMBER IS A PRIME NUMBER

# The IsPrime function checks if a given number is prime.
def IsPrime(num):
    return num > 1 and all(num % i != 0 for i in range(2, int(num ** 0.5) + 1))
# Example usage
print(IsPrime(13))
# Output: True
print(IsPrime(4))
# Output: False