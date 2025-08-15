# MARATHON DISTANCE CHECKER

# The marathon_distance function helps Mary determine if the marathon she wants
# to run is exactly 25 miles long by analyzing the lengths listed in small portions on the
# sign-up sheet. It returns true if the total distance matches 25 miles, otherwise, it
# returns false.

def marathon_distance(distances): return sum(map(abs,
distances)) == 25
distances = [1, 2, -3, 4, 5, -6, 7, 8, -9, 10]
print(marathon_distance(distances))
# Output: False