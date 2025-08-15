# TRUNCATE A STRING TO A GIVEN LENGTH

# The truncate_string function truncate a string to a given length.

def truncate_string(s, max_length):
    return s[:max_length] + '...' if len(s) > max_length else s
# Example usage
print(truncate_string("Hello, world!", 5))
# Output: Hello...