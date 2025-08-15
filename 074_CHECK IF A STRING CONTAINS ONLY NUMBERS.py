# CHECK IF A STRING CONTAINS ONLY NUMBERS

# The ContainsOnlyNumbers function checks if a given string contains only numeric characters.

import re
def ContainsOnlyNumbers(s): return bool(re.match(r'^\d+$', s))
# Example usage
print(ContainsOnlyNumbers("12345"))
# Output: True
print(ContainsOnlyNumbers("12a34"))
# Output: False