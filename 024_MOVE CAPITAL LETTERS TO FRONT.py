# MOVE CAPITAL LETTERS TO FRONT

# The cap_to_front function moves all capital letters in a word to the front of the
# word, preserving their original order, and followed by the lowercase letters.

def cap_to_front(s): return ''.join(filter(str.isupper, s)) + ''.join(filter(str.islower, s))
print(cap_to_front("MoveCapitalLettersToFront"))
# Output: MCLFoveapitalettersoront