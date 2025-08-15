# FIND THE DAY OF YEAR

# The day_of_year function takes a date as
# input and calculates the day of the year for
# that date.
from datetime import datetime

def day_of_year(date): return date.timetuple().tm_yday
print(day_of_year(datetime(2024, 10, 1)))
# Output: 275