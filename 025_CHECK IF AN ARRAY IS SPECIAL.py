# CHECK IF AN ARRAY IS SPECIAL
#
# The is_special_array function determines whether an array is special, where every
# even index contains an even number and every odd index contains an odd number.

def is_special_array(arr): return all(arr[i] % 2 == i % 2 for i in range(len(arr)))
arr = [2, 3, 6, 8, 9]
print(is_special_array(arr))
# Output: False