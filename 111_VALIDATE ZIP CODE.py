'''
Problem    : VALIDATE ZIP CODE
Description: The is_valid function validates whether a given string is a valid zip code.
@Author    : Dr. J. K. Verma
@Date      : 2025-09-20
'''


import re
def is_valid(zip_code): return bool(re.match(r'^\d{5}$', zip_code))
# Example usage
print(is_valid("12345"))
# Output: True
print(is_valid("1234"))
# Output: False
print(is_valid("123456"))
# Output: False
print(is_valid("12 45"))
# Output: False