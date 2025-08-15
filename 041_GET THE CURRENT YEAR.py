# GET THE CURRENT YEAR
# The current_year function returns the current year as an integer.

from datetime import datetime
def current_year(): return datetime.now().year
print(current_year())
# Output: e.g., 2024