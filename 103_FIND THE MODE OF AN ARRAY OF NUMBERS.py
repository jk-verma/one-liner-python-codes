# FIND THE MODE OF AN
# ARRAY OF NUMBERS

# The mode function finds the mode of an array of numbers.

def mode(arr):
    occurrences = {}
    for num in arr:
        if num in occurrences:
            occurrences[num] += 1
        else:
            occurrences[num] = 1
            max_occurrences = max(occurrences.values())
    return [num for num, count in occurrences.items() if count == max_occurrences]
# Example usage
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
print(f"Mode: {mode(numbers)}")
# Output: Mode: [4]