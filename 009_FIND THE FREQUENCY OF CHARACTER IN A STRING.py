'''
Problem    : FIND THE FREQUENCY OF CHARACTER IN A STRING
Description: The character_frequency function finds the frequency of characters in a String.
@Author    : Dr. J. K. Verma
@Date      : 2025-08-15
@Version   : 1.0
'''

def character_frequency(string): return {char: string.count(char) for char in set(string)}

print(", ".join([f"{k}=>{v}" for k, v in character_frequency("hello").items()]))
# Output: h=>1, e=>1, l=>2, o=>1