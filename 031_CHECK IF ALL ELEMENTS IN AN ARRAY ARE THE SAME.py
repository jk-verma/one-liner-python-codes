'''
Problem    : CHECK IF ALL ELEMENTS IN AN ARRAY ARE THE SAME
Description: The test_jackpot function takes in a string representing the result of a
             jackpot game and returns true if all elements in the string are the same,
             indicating a jackpot, and false otherwise.
@Author    : Dr. J. K. Verma
@Date      : 2025-08-15
@Version   : 1.0
'''

def test_jackpot(result): return len(set(result)) == 1
result = "22222"
print(test_jackpot(result))
# Output: True