# REMOVE DUPLICATES FROM A STRING

# The remove_duplicates_from_string function removes duplicates from a String.

def remove_duplicates_from_string(string):
    return ''.join(sorted(set(string), key=string.index))
# Example usage
print(remove_duplicates_from_string("hello"))
# Output: helo