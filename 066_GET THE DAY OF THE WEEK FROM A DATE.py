# GET THE DAY OF THE WEEK FROM A DATE

# The GetDayOfWeek function get the day
# of the week from a date.

from datetime import datetime
def GetDayOfWeek(date_str):
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    return date_obj.strftime('%A')
# Example usage
print(GetDayOfWeek("2023-08-02"))
# Output: Wednesday