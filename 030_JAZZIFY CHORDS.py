# JAZZIFY CHORDS

# The jazzified_arr function appends the number 7 to the end of every chord in an array.
# It ignores all chords that already end with 7.

def jazzify(arr): return [x if str(x)[-1] == '7' else x + 7 for x in arr]
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
jazzified_arr = jazzify(arr)
print(", ".join(map(str, jazzified_arr)))
# Output: 8, 9, 10, 11, 12, 13, 7, 15, 16