# CONVERT MINUTES TO HOURS AND MINUTES

# The mins_to_hours_and_mins function convert minutes to hours and minutes.

def mins_to_hours_and_mins(mins):
    return f"{mins // 60} hours and {mins % 60} minutes"
# Example usage
print(mins_to_hours_and_mins(150))
# Output: 2 hours and 30 minutes