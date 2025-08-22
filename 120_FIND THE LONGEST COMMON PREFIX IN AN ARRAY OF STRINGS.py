'''
Problem    : FIND THE LONGEST COMMON PREFIX IN AN ARRAY OF STRINGS
Description: The longest_common_prefix function finds the longest common prefix among an
             array of strings.
@Author    : Dr. J. K. Verma
@Date      : 2025-09-20
'''


def longest_common_prefix(strs):
    return "" if not strs \
        else "".join(c for i, c in enumerate(strs[0]) if all(s[i] == c for s in strs))
# Test
strs = ["apple", "apricot", "appetizer"]
print(longest_common_prefix(strs))
# Output: "ap"