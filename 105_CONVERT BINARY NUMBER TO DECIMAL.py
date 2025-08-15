# CONVERT BINARY NUMBER TO DECIMAL

# The binary_to_decimal function converts a binary number to decimal.

def binary_to_decimal(binary):
    return sum(int(bit) * 2**index for index, bit in enumerate(reversed(binary)))
# Example usage
print(binary_to_decimal("1101"))
# Output: 13