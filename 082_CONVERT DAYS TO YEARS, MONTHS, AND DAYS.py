# CONVERT DAYS TO YEARS, MONTHS, AND DAYS

# The DaysToYearsMonthsDays function converts a given number of days to years,
# months, and remaining days.
def DaysToYearsMonthsDays(days):
    years = days // 365
    months = (days % 365) // 30
    remaining_days = (days % 365) % 30
    return f"{years} years, {months} months, and {remaining_days} days"
# Example usage
print(DaysToYearsMonthsDays(1000))
# Output: 2 years, 9 months, and 5 days