# JOIN PATH PORTIONS

# The join_path function receives two portions of a path and joins them using the
# "/" separator. If the separator is missing between the portions, it is added before
# joining.

def join_path(portion1, portion2):
    return f"{portion1.rstrip('/')}/{portion2.lstrip('/')}"
# Example usage
print(join_path("portion1", "portion2"))
# Output: portion1/portion2