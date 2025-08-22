'''
Problem    : COUNT THE NUMBER OF WORDS IN A STRING
Description: The count_words function counts the number of words in a given string.
@Author    : Dr. J. K. Verma
@Date      : 2025-08-15
@Version   : 1.0
'''

def count_words(string): return len(string.split())
print(count_words("Hello world, how are you?"))
# Output: 5