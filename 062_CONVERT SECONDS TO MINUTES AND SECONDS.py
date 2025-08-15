# CONVERT SECONDS TO MINUTES AND SECONDS

# The SecsToMinsAndSecs function calculate the number of minutes and remaining
# seconds and then returns a formatted string containing the result.

def SecsToMinsAndSecs(seconds):
    return f"{seconds // 60} minutes and {seconds % 60} seconds"
# Example usage
print(SecsToMinsAndSecs(120))
# Output: 2 minutes and 0 seconds