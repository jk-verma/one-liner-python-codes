# CAPITALIZE A STRING
# The capitalize_string function takes a
# string as input and capitalizes the first
# character.

def capitalize_string(s): return s[0].upper() + s[1:] if s else ""
print(capitalize_string("follow for more"))
# Output: Follow for more