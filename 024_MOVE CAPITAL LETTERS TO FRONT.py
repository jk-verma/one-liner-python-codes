'''
Problem    : MOVE CAPITAL LETTERS TO FRONT
Description: The cap_to_front function moves all capital letters in a word to the front of the word, preserving their original order, and followed by the lowercase letters.
@Author    : Dr. J. K. Verma
@Date      : 2025-08-15
@Version   : 1.0
'''


def cap_to_front(s): return ''.join(filter(str.isupper, s)) + ''.join(filter(str.islower, s))
print(cap_to_front("MoveCapitalLettersToFront"))
# Output: MCLFoveapitalettersoront