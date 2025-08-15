# FIND THE NUMBER OF DAYS BETWEEN TWO DAYS

# The day_diff function finds the number of
# days between two days.

from datetime import datetime

def day_diff(date1, date2): return abs((date2 - date1).days) + 1
date1 = datetime(2020, 10, 21)
date2 = datetime(2021, 10, 22)
print(day_diff(date1, date2))
# Output: 367