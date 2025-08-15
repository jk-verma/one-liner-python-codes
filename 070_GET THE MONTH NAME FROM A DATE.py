# GET THE MONTH NAME FROM
# A DATE
# The GetMonthName function retrieves
# the name of the month from a given date.

import datetime
def GetMonthName(date):
    return date.strftime("%B")
# Example usage
date = datetime.datetime(2023, 8, 2)
print(GetMonthName(date))
# Output: August