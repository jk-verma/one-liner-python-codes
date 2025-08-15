# VALIDATE VOWEL SANDWICH

# The is_vowel_sandwich function validates
# whether a 3-character string is a vowel
# sandwich.
def is_vowel_sandwich(string): return (len(string) == 3 and
                                       string[0] not in 'aeiou' and
                                       string[1] in 'aeiou' and string[2]) not in 'aeiou'
print(is_vowel_sandwich("bat"))
# Output: False
print(is_vowel_sandwich("cat"))
# Output: True
print(is_vowel_sandwich("dog"))
# Output: False