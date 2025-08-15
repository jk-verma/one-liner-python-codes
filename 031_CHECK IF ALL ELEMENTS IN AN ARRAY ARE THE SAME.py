# CHECK IF ALL ELEMENTS IN AN ARRAY ARE THE SAME

# The test_jackpot function takes in a string representing the result of a jackpot game
# and returns true if all elements in the string are the same, indicating a jackpot, and
# false otherwise.

def test_jackpot(result): return len(set(result)) == 1
result = "22222"
print(test_jackpot(result))
# Output: True