# CHECK IF AN ARRAY CONTAINS ONLY UNIQUE VALUES

# The HasUniqueValues function converts the array arr to a set using uniq, which
# removes duplicate elements.

def HasUniqueValues(arr): return len(set(arr)) == len(arr)
# Example usage
print(HasUniqueValues([1, 2, 3, 4, 5]))
# Output: True
print(HasUniqueValues([1, 2, 3, 4, 4]))
# Output: False