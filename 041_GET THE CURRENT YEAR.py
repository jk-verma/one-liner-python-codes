'''
Problem    : GET THE CURRENT YEAR
Description: The current_year function returns the current year as an integer.
@Author    : Dr. J. K. Verma
@Date      : 2025-08-15
@Version   : 1.0
'''

from datetime import datetime
def current_year(): return datetime.now().year
print(current_year())
# Output: e.g., 2024