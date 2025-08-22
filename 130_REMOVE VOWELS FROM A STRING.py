'''
Problem    : REMOVE VOWELS FROM A STRING
Description: The remove_vowels function removes vowels from a string.
@Author    : Dr. J. K. Verma
@Date      : 2025-08-25
'''

import re
def remove_vowels(string):
    return re.sub(r'[aeiouAEIOU]', '', string)
# Test case
print(remove_vowels("Hello, World!"))
# Output: "Hll, Wrld!"