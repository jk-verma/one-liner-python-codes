# CREATE RANDOM STRINGS
# The random_string function generates a
# random String of lowercase letters with the
# specified length.
import random
import string

def random_string(length): return ''.join(random.choice(string.ascii_lowercase) for _ in
                                          range(length))
print(random_string(10))
# Output: e.g., bjmfpwmoqi