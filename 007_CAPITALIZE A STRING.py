'''
Problem    : CAPITALIZE A STRING
Description: The capitalize_string function takes a string as input and
             capitalizes the first character.
@Author    : Dr. J. K. Verma
@Date      : 2025-08-15
@Version   : 1.0
'''

def capitalize_string(s):
    return s[0].upper() + s[1:] if s else ""
print(capitalize_string("follow for more"))
# Output: Follow for more