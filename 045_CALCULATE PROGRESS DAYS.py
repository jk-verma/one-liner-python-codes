# CALCULATE PROGRESS DAYS

# The progress_days function calculates the total number of progress days based on an
# array of miles run every Saturday.

def progress_days(runs): return sum(runs[i] < runs[i + 1] for i in range(len(runs) - 1))
runs = [3, 4, 1, 2, 4, 5]
print(progress_days(runs))
# Output: 3