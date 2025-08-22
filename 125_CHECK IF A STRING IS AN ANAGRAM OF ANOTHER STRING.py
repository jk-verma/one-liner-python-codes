'''
Problem    : CHECK IF A STRING IS AN ANAGRAM OF ANOTHER STRING
Description: The is_anagram function checks if a string is an anagram of another string.
@Author    : Dr. J. K. Verma
@Date      : 2025-09-20
'''

def is_anagram(str1, str2):
    return sorted(str1) == sorted(str2)
print(is_anagram("listen", "silent"))
# Output: True
print(is_anagram("hello", "world"))
# Output: False