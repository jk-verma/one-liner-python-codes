# GET THE CURRENT MONTH (0-BASED INDEX)

# The CurrentMonth retrieves the current month as a 0-based index.

from datetime import datetime
def CurrentMonth():
    return datetime.now().month - 1
# Example usage
print(CurrentMonth())
# Output: 3 is the current month (0-based index)