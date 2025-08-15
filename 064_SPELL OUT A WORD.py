# SPELL OUT A WORD

# The Spelling function takes a word as input and spells it out by consecutively
# adding letters until the full word is completed. It then returns an array
# containing each step of the spelling process.

def Spelling(word):
    return [word[:i+1] for i in range(len(word))]
# Example usage
word = "example"
spelled_word = Spelling(word)
print(", ".join(spelled_word))
# Output: e, ex, exa, exam, examp, exampl, example