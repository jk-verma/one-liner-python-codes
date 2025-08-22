'''
Problem    : CHECK IF A STRING STARTS WITH A SPECIFIC CHARACTER
Description: The starts_with_char function checks if a given string starts with a specific character.
@Author    : Dr. J. K. Verma
@Date      : 2025-08-15
@Version   : 1.0
'''
def starts_with_char(string, char): return string.lower().startswith(char.lower())
print(starts_with_char("Hello, world!", 'H'))
# Output: True
print(starts_with_char("Hello, world!", 'h'))
# Output: True