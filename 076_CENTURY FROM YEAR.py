# CENTURY FROM YEAR

# The CenturyFromYear function calculates the century corresponding to a given year.
# It takes a year as input and returns its corresponding century.

def CenturyFromYear(year):
    return (year + 99) // 100
# Example usage
print(CenturyFromYear(1905)) # Output: 20
print(CenturyFromYear(1700)) # Output: 17
print(CenturyFromYear(1988)) # Output: 20
print(CenturyFromYear(2000)) # Output: 20
print(CenturyFromYear(2001)) # Output: 21