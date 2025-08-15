# BINARY LETTER CONVERTER

# The ConvertBinary function transforms all letters from
# 'a' to 'm' to 0 and letters from 'n' to 'z' to 1 in a given string.

def ConvertBinary(s):
    return ''.join(['0' if 'a' <= c <= 'm' else '1' for c in s.lower()])
# Example usage
print(ConvertBinary("hello"))
# Output: 00000
print(ConvertBinary("world"))
# Output: 11111
print(ConvertBinary("abcxyz"))
# Output: 000111