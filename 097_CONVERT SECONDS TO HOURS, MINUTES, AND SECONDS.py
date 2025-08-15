# CONVERT SECONDS TO HOURS, MINUTES, AND SECONDS

# The seconds_to_hours_mins_secs function convert seconds to hours, minutes, and remaining seconds.

def seconds_to_hours_mins_secs(seconds):
    hours = seconds // 3600
    remaining_seconds = seconds % 3600
    minutes = remaining_seconds // 60
    remaining_minutes = remaining_seconds % 60
    return f"{hours} hours, {minutes} minutes, and {remaining_minutes} seconds"
# Example usage
print(seconds_to_hours_mins_secs(7320))
# Output: "2 hours, 2 minutes, and 0 seconds"