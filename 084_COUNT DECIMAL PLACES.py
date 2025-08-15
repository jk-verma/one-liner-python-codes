# COUNT DECIMAL PLACES
# The GetDecimalPlaces function takes a
# number represented as a string and returns
# the number of decimal places it has. If the
# number has no decimal places, it returns 0.
def GetDecimalPlaces(num):
    if "." in num:
        return len(num.split(".")[1])
    else:
        return 0
# Example usage
print(GetDecimalPlaces("3.14159"))
# Output: 5
print(GetDecimalPlaces("100.345"))
# Output: 3
print(GetDecimalPlaces("10.000"))
# Output: 3
print(GetDecimalPlaces("32"))
# Output: 0