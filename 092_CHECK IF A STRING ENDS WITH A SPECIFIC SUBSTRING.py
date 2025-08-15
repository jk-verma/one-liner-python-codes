# CHECK IF A STRING ENDS WITH A SPECIFIC SUBSTRING

# The ends_with_substring function checks if a string ends with a specific substring.

def ends_with_substring(string, substring): return string.endswith(substring)
# Example usage
print(ends_with_substring("Hello, world!", "world!"))
# Output: True
print(ends_with_substring("Hello, world!", "Hello"))
# Output: False