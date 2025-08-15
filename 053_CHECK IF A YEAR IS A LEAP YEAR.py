# CHECK IF A YEAR IS A LEAP YEAR

# The is_leap_year function takes a year as input and returns
# true if it's a leap year and false otherwise.

def is_leap_year(year): return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
# Example usage
print(is_leap_year(2024))
# Output: True
print(is_leap_year(2023))
# Output: False