# REMOVE WHITESPACE FROM A STRING

# The RemoveWhitespace function removes all whitespace characters from a given string.

def RemoveWhitespace(str):
    return "".join(str.split())
# Example usage
print(RemoveWhitespace(" Hello, world! "))
# Output: Hello,world!