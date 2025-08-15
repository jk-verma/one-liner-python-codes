# CONVERT VIDEO LENGTH TO SECONDS

# The minutes_to_seconds function takes the length of a video in the format "mm:ss"
# and converts it to seconds. If the input format is correct, it returns the length of
# the video in seconds; otherwise, it returns 0.

def minutes_to_seconds(time):
    minutes, seconds = map(int, time.split(':'))
    return minutes * 60 + seconds if 0 <= seconds < 60 else 0
# Example usage
print(minutes_to_seconds("02:54"))
# Output: 174