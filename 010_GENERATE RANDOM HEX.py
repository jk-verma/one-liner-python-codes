'''
Problem    : GENERATE RANDOM HEX
Description: The random_hex function generates a random integer between 0 and 16777215 (0xffffff in hexadecimal).
@Author    : Dr. J. K. Verma
@Date      : 2025-08-15
@Version   : 1.0
'''



import random

def random_hex(): return f"#{random.randint(0,
0xFFFFFF):06X}"

print(random_hex())
# Output: e.g., #A58E72