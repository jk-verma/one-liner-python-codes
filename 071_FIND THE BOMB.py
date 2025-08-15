# FIND THE BOMB

# The Bomb function searches for the word "bomb" in a given string. If the word is
# found, it returns "Duck!!!", indicating a potential danger. Otherwise, it returns
# "There is no bomb, relax.", reassuring that there is no threat.
import re
def Bomb(s):
    return "Duck!!!" if re.search(r'\bbomb\b', s, re.IGNORECASE) else "There is no bomb, relax."
# Example usage
s = "The bomb is about to explode."
print(Bomb(s))
# Output: Duck!!!