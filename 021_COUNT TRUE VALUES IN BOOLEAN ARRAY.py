# COUNT TRUE VALUES IN BOOLEAN ARRAY

# The count_true function counts the number of true values in a boolean array.

def count_true(lst): return sum(1 for x in lst if x)
bool_array = [True, False, True, False, True]
count = count_true(bool_array)
print("Number of true values:", count)
# Output: Number of true values: 3