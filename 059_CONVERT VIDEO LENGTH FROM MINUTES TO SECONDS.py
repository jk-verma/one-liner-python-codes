# CONVERT VIDEO LENGTH FROM MINUTES TO SECONDS

# The minutes_to_seconds function takes the length of a video in the
# format "mm:ss" and converts it into seconds.

def minutes_to_seconds(time):
    return sum(int(x) * 60 ** i for i, x in
enumerate(reversed(time.split(':'))))
# Example usage
print(minutes_to_seconds("02:54"))
# Output: 174