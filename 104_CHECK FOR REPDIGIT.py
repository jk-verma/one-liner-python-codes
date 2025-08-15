# CHECK FOR REPDIGIT

# The is_repdigit function checks if a given integer is a repdigit, meaning it is
# composed of the same digit repeated. If # the integer is a repdigit, it
# returns true; otherwise, it returns false.

def is_repdigit(num):
    return len(set(str(num))) == 1
# Example usage
print(is_repdigit(333))
# Output: True