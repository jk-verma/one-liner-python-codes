'''
Problem    : FIND THE DAY OF YEAR
Description: The day_of_year function takes a date as input and calculates the day of the year for that date.
@Author    : Dr. J. K. Verma
@Date      : 2025-08-15
@Version   : 1.0
'''
from datetime import datetime

def day_of_year(date): return date.timetuple().tm_yday
print(day_of_year(datetime(2024, 10, 1)))
# Output: 275