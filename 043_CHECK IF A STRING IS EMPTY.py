'''
Problem    : CHECK IF A STRING IS EMPTY
Description: The empty_string function checks if a string is empty.
@Author    : Dr. J. K. Verma
@Date      : 2025-08-15
@Version   : 1.0
'''

def empty_string(string): return not string.strip()
print(empty_string(""))
# Output: True
print(empty_string("Hello, world!"))
# Output: False