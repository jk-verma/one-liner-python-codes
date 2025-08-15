# FIND THE DIFFERENCE BETWEEN TWO DATES IN DAYS

# The DateDifferenceInDays function finds the difference between two dates in days.

from datetime import datetime
def DateDifferenceInDays(date1, date2):
    return (date2 - date1).days
# Example usage
startDate = datetime(2023, 8, 1)
endDate = datetime(2023, 8, 10)
print(DateDifferenceInDays(startDate, endDate))
# Output: 9