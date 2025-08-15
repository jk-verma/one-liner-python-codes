# FIND NEMO

# The find_nemo function function takes a string of words as input
# and searches for the word "Nemo". If "Nemo" is found, it returns
# a string indicating the position of "Nemo" in the sentence. If "Nemo"
# is not found, it returns a message indicating its absence.

def find_nemo(sentence):
    words = sentence.split()
    index = words.index("Nemo") + 1 if "Nemo" in words else -1
    return f"I found Nemo at {index}!" if index > 0 else "I can't find Nemo :("
# Example usage
print(find_nemo("I am finding Nemo"))
# I found Nemo at 3!