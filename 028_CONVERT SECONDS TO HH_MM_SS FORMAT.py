'''
Problem    : CONVERT SECONDS TO HH:MM:SS FORMAT
Description: The seconds_to_hhmmss function converts the given number of seconds into
             the HH:MM:SS format.
@Author    : Dr. J. K. Verma
@Date      : 2025-08-15
@Version   : 1.0
'''


def seconds_to_hhmmss(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f"{hours:02}:{minutes:02}:{seconds:02}"
print(seconds_to_hhmmss(3660))
# Output: 01:01:00