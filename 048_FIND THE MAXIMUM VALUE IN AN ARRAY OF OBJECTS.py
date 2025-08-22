'''
FIND THE MAXIMUM VALUE IN AN ARRAY OF OBJECTS
The FindMaxValue function finds the maximum value in an array of objects.
@Author    : Dr. J. K. Verma
@Date      : 2025-08-15
@Version   : 1.0
'''

def find_max_value(arr, key): return max(item[key] for item in arr)
# Example usage
arr = [
{"name": "Alice", "score": 80},
{"name": "Bob", "score": 95},
{"name": "Charlie", "score": 70}
]
print(find_max_value(arr, "score"))
# Output: 95