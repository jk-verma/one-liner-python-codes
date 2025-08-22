'''
Problem    : SHUFFLE THE CHARACTERS OF A STRING
Description: The shuffle_string function suffle the characters of a String.
@Author    : Dr. J. K. Verma
@Date      : 2025-09-20
'''
import random
def shuffle_string(s):
    shuffled_chars = list(s)
    random.shuffle(shuffled_chars)
    return ''.join(shuffled_chars)
# Example usage:
s = "hello"
shuffled_string = shuffle_string(s)
print(f"Output: {shuffled_string}")
# Output: oelhl