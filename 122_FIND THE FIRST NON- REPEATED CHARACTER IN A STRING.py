'''
Problem    : FIND THE FIRST NON-REPEATED CHARACTER IN A STRING
Description: The first_non_repeated_char function finds the first non-repeated character in a String.
@Author    : Dr. J. K. Verma
@Date      : 2025-09-20
'''

def first_non_repeated_char(s): return next((c for c in s if s.count(c) == 1), None)
s = "abacabad"
print(first_non_repeated_char(s))
# Output: c