# FIND THE AVERAGE OF EVEN NUMBERS IN AN ARRAY

# The average_of_even_numbers function finds the average of even numbers in an array.

def average_of_even_numbers(arr):
    even_numbers = [num for num in arr if num % 2 == 0]
    return sum(even_numbers) / len(even_numbers) if even_numbers else 0
# Example usage
print(average_of_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9,
10]))
# Output: 6.0