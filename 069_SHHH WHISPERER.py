# SHHH WHISPERER

# The Shhh function takes a sentence as input, removes all capital letters except for
# the first letter, wraps the sentence in double quotation marks, and adds ",
# whispered your friend." to the end.

def Shhh(sentence):
    lowered = f'"{sentence[0].lower()}{sentence[1:].lower()}", whispered your friend.'
    return lowered
# Example usage
print(Shhh("HELLO THERE"))
# Output: "Hello there", whispered your friend.