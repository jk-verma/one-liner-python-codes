# MATCHSTICK COUNT IN STEPS

# The match_houses function calculates the
# total number of matchsticks required based
# on the number of steps provided.

def match_houses(steps): return steps * 6 - (steps - 1) if steps > 0 else 0
print(match_houses(1))
# Output: 6
print(match_houses(4))
# Output: 21
print(match_houses(0))
# Output: 0