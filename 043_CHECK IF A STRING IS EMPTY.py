# CHECK IF A STRING IS EMPTY
# The empty_string function checks if a string is empty.

def empty_string(string): return not string.strip()
print(empty_string(""))
# Output: True
print(empty_string("Hello, world!"))
# Output: False