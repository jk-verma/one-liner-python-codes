# GET THE CURRENT DATE IN DD/MM/YYYY FORMAT

# The get_current_date function returns the current date in the format "DD/MM/YYYY".

from datetime import datetime
def get_current_date(): return datetime.now().strftime("%d/%m/%Y")
print(get_current_date())
# Output: e.g., 16/04/2024