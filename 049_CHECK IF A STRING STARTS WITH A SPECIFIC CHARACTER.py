# CHECK IF A STRING STARTS WITH A SPECIFIC CHARACTER

# The starts_with_char function checks if a
# given string starts with a specific character.
def starts_with_char(string, char): return string.lower().startswith(char.lower())
print(starts_with_char("Hello, world!", 'H'))
# Output: True
print(starts_with_char("Hello, world!", 'h'))
# Output: True